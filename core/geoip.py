from django.conf import settings
import pygeoip

geoip = pygeoip.GeoIP(settings.GEOIP_DAT)
