from urllib.request import urlopen
from django.db import transaction

from .models import Server, Player


@transaction.atomic
def refresh_servers():
    Server.objects.pre_refresh()
    Player.objects.pre_refresh()

    source = urlopen(
        'http://www.qtracker.com/server_list_details.php?game=vietcong'
    )
    lines = source.readlines()
    conns = [str(line, encoding='utf8').split(':')
             for line in lines if line.strip()]
    for conn in conns:
        server, _ = Server.objects.get_or_create(
            ip=conn[0],
            infoport=int(conn[1]),
        )

    # some servers might not come from Qtracker
    for server in Server.objects.all():
        server.refresh()

    Server.objects.post_refresh()
    Player.objects.post_refresh()
