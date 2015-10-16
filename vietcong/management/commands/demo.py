from django.core.management.base import BaseCommand

from game import factories

MODES = 6
MAPS = 40
SERVERS = 20


def populate():
    [factories.Mode() for _ in range(MODES)]
    [factories.Map() for _ in range(MAPS)]
    [factories.Server() for _ in range(SERVERS)]


class Command(BaseCommand):
    help = 'Populates DB with a demo (random) content.'

    def handle(self, *args, **options):
        populate()
