from urllib.request import urlopen

from . import models


def refresh_servers():
    source = urlopen(
        'http://www.qtracker.com/server_list_details.php?game=vietcong'
    )
    lines = source.readlines()
    conns = [str(line, encoding='utf8').split(':')
             for line in lines if line.strip()]
    for conn in conns:
        server, _ = models.Server.objects.get_or_create(
            ip=conn[0],
            infoport=int(conn[1]),
        )
        server.refresh()

def delete_duplicate_servers():
    for server in models.Server.objects.all():
        if server.pk:  # so it's not already deleted
            models.Server.objects \
                    .filter(ip=server.ip, infoport=server.infoport) \
                    .exclude(pk=server.pk) \
                    .delete()
