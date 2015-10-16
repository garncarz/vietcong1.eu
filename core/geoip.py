from django.conf import settings
import pygeoip

class Dummy:
    def __getattr__(self, _):
        return lambda: None

geoip = pygeoip.GeoIP(settings.GEOIP_DAT) if hasattr(settings, 'GEOIP_DAT') \
        else Dummy()
