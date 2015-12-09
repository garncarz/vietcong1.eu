from django.conf import settings
import pygeoip

class Dummy:
    def __getattr__(self, _):
        return lambda _: ''  # gettext can't handle None, it seems

geoip = pygeoip.GeoIP(settings.GEOIP_DAT) if hasattr(settings, 'GEOIP_DAT') \
        else Dummy()
