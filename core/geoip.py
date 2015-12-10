from django.conf import settings
import pygeoip

class Dummy:
    def __getattr__(self, _):
        return lambda _: ''  # gettext can't handle None, it seems


if getattr(settings, 'GEOIP_DAT', None):
    geoip = pygeoip.GeoIP(settings.GEOIP_DAT)
else:
    geoip = Dummy()
