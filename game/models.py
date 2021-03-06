from datetime import timedelta
import logging
import os.path
import re
import socket
from uuid import uuid4

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from core import geoip


logger = logging.getLogger(__name__)


class Mode(models.Model):
    name = models.CharField(max_length=256, unique=True)

    __str__ = lambda self: str(self.name)


class Map(models.Model):
    name = models.CharField(max_length=256, unique=True)
    modes = models.ManyToManyField(Mode)

    __str__ = lambda self: str(self.name)

    def get_absolute_url(self):
        return reverse('game:map_detail', kwargs={'pk': self.pk})


class MapImage(models.Model):
    def upload_to(instance, filename):
        return '%s/%s%s' % (slugify(instance.map.name),
                            uuid4(),
                            os.path.splitext(filename)[1])

    image = models.ImageField(upload_to=upload_to)
    map = models.ForeignKey(Map, related_name='images')

    __str__ = lambda self: str(self.image.url)


class ServerQuerySet(models.QuerySet):
    def online(self):
        return self.filter(online=True)


class ServerManager(models.Manager):
    def pre_refresh(self):
        self.model.objects.update(online=False)

    def post_refresh(self):
        self.model.objects \
            .filter(online=False, offline_since=None) \
            .update(offline_since=timezone.now())
        self.model.objects \
            .filter(offline_since__lt=timezone.now() - timedelta(hours=1)) \
            .delete()
        self.delete_duplicates()

    def delete_duplicates(self):
        for server in self.model.objects.all():
            if server.pk:  # so it's not already deleted
                self.model.objects \
                    .filter(ip=server.ip, infoport=server.infoport) \
                    .exclude(pk=server.pk) \
                    .delete()


class Server(models.Model):
    objects = ServerManager.from_queryset(ServerQuerySet)()

    ip = models.GenericIPAddressField()
    infoport = models.PositiveSmallIntegerField(default=15425)
    port = models.PositiveSmallIntegerField(default=5425)

    name = models.CharField(max_length=256)
    map = models.ForeignKey(Map, null=True, blank=True,
                            related_name='servers')
    mode = models.ForeignKey(Mode, null=True, blank=True)

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
    online_since = models.DateTimeField(default=timezone.now)
    offline_since = models.DateTimeField(null=True, blank=True)

    __str__ = lambda self: '%s (%s:%s)' % (self.name, self.ip, self.port)
    tcpip = property(lambda self: '%s:%s' % (self.ip, self.infoport))

    def get_absolute_url(self):
        return reverse('game:server_detail',
                       kwargs={'ip': self.ip, 'port': self.port})

    def refresh(self):
        try:
            info = self._fetch_info()
            self._merge_info(info)
            self._merge_players_info(info)
        except:
            logger.exception('Error refreshing server %s' % self.tcpip)
            self.online = False
            self.save()

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
        self.country_name = geoip.country_name_by_addr(self.ip)

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
                player, _ = Player.objects.get_or_create(server=self,
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


class PlayerManager(models.Manager):
    def pre_refresh(self):
        self.model.objects.update(online=False)

    def post_refresh(self):
        self.model.objects.filter(online=False).delete()


class Player(models.Model):
    objects = PlayerManager()

    name = models.CharField(max_length=256)
    ping = models.PositiveSmallIntegerField(default=0)
    frags = models.PositiveSmallIntegerField(default=0)

    server = models.ForeignKey(Server, related_name='players')

    online = models.BooleanField(default=True)
    online_since = models.DateTimeField(default=timezone.now)

    __str__ = lambda self: '%s@%s' % (self.name, self.server.name)
