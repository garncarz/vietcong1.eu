from django.core.management.base import BaseCommand

from game import factories

MODES = 6
MAPS = 40
SERVERS = 20


class Command(BaseCommand):
    help = 'Populates DB with a demo (random) content.'

    def handle(self, *args, **options):
        self.stdout.write('Creating %d modes...' % MODES)
        [factories.Mode() for _ in range(MODES)]

        self.stdout.write('Creating %d maps...' % MAPS)
        [factories.Map() for _ in range(MAPS)]

        self.stdout.write('Creating %d servers...' % SERVERS)
        [factories.Server() for _ in range(SERVERS)]
