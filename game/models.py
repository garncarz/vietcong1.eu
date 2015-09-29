import re
import socket

from django.conf import settings
from django.db import models

from core import geoip

class Mode(models.Model):
    name = models.CharField(max_length=256, unique=True)


class Map(models.Model):
    name = models.CharField(max_length=256, unique=True)
    modes = models.ManyToManyField(Mode)


class Server(models.Model):
    ip = models.GenericIPAddressField()
    infoport = models.PositiveSmallIntegerField(default=15425)
    port = models.PositiveSmallIntegerField(default=5425)

    name = models.CharField(max_length=256)
    map = models.ForeignKey(Map)
    mode = models.ForeignKey(Mode)

    country = models.CharField(max_length=2, null=True, blank=True)
    country_name = models.CharField(max_length=50, null=True, blank=True)

    version = models.CharField(max_length=4)
    hradba = models.CharField(max_length=4, null=True, blank=True)
    numplayers = models.PositiveSmallIntegerField(default=0)
    maxplayers = models.PositiveSmallIntegerField(default=0)

    password = models.BooleanField(default=False)
    dedic = models.BooleanField(default=False)
    vietnam = models.BooleanField(default=False)

    online = models.BooleanField(default=True)
    online_since = models.DateTimeField(auto_now_add=True)
    offline_since = models.DateTimeField(null=True, blank=True)

    def refresh(self):
        info = self._fetch_info()
        self._merge_info(info)
        self._merge_players_info(info)

    def _fetch_info(self):
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp.settimeout(settings.UDP_TIMEOUT)
        udp.connect((self.ip, self.infoport))
        udp.send('\\status\\players\\'.encode('ascii'))
        data = udp.recv(4096).decode('ascii')
        arr = re.split('\\\\', data)[1:-4]
        return dict(zip(arr[::2], arr[1::2]))

    def _merge_info(self, info):
        self.online = True
        self.offlineSince = None

        self.port = int(info['hostport'])
        self.password = 'password' in info
        self.dedic = 'dedic' in info
        self.vietnam = 'vietnam' in info

        self.country = geoip.country_code_by_addr(self.ip)
        self.countryname = geoip.country_name_by_addr(self.ip)

        self.name = info['hostname']

        self.map, self.mode = self._merge_map_info(info)

        self.version = (lambda v: v[0] + '.' + v[1:])(info['uver'])
        self.maxplayers = info['maxplayers']
        self.hradba = info['hbver'] if 'hbver' in info else None

        self.save()

    def _merge_map_info(self, info):
        _map, _ = Map.objects.get_or_create(name=info['mapname'])
        mode, _ = Mode.objects.get_or_create(name=info['gametype'])

        if not _map.modes.filter(pk=mode.pk).exists():
            _map.modes.add(mode)

        return (_map, mode)

    def _merge_players_info(self, info):
        count = 0
        for i in range(int(info['numplayers'])):
            try:
                name = info['player_' + str(i)]
                player = Player.objects.get_or_create(server=self,
                                                      name=name,
                                                      online=False)
                player.online = True
                player.ping = int(info['ping_' + str(i)])
                player.frags = int(info['frags_' + str(i)])
                player.save()
                count += 1
            except KeyError:
                break

        self.numplayers = count
        self.save()


class Player(models.Model):
    name = models.CharField(max_length=256)
    ping = models.PositiveSmallIntegerField()
    frags = models.PositiveSmallIntegerField()

    server = models.ForeignKey(Server)

    online = models.BooleanField(default=True)
    online_since = models.DateTimeField(auto_now_add=True)
