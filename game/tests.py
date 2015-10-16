from core.tests import TestCase
from vietcong.management.commands.demo import populate

from . import models

class ViewsTestCase(TestCase):
    def setUp(self):
        populate()

    def test_server_list(self):
        resp = self.get('game:server_list')
        self.assert200(resp, 'game/server_list.html')
        self.assertTrue(len(resp.context['server_list']) > 0)

    def test_server_detail(self):
        server = models.Server.objects.first()
        resp = self.get('game:server_detail', {'ip': server.ip,
                                               'port': server.port})
        self.assert200(resp, 'game/server_detail.html')
        self.assertTrue(resp.context['server'].pk == server.pk)

    def test_player_list(self):
        resp = self.get('game:player_list')
        self.assert200(resp, 'game/player_list.html')
        self.assertTrue(len(resp.context['player_list']) > 0)

    def test_map_detail(self):
        _map = models.Map.objects.first()
        resp = self.get('game:map_detail', {'pk': _map.pk})
        self.assert200(resp, 'game/map_detail.html')
        self.assertTrue(resp.context['map'].pk == _map.pk)
