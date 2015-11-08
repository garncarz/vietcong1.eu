from django.core.management.base import BaseCommand

from game import factories

MODES = 6
MAPS = 40
SERVERS = 20


class Command(BaseCommand):
    help = 'Populates DB with a demo (random) content.'

    def print(self, msg):
        if getattr(self, 'verbose', None):
            self.stdout.write(msg)

    def handle(self, *args, **options):
        self.verbose = 0 if 'verbosity' not in options \
                       else options['verbosity']

        self.print('Creating %d modes...' % MODES)
        [factories.Mode() for _ in range(MODES)]

        self.print('Creating %d maps...' % MAPS)
        [factories.Map() for _ in range(MAPS)]

        self.print('Creating %d servers...' % SERVERS)
        [factories.Server() for _ in range(SERVERS)]


def populate():
    Command().execute(options={'verbosity': 0})
