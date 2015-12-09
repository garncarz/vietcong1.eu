from __future__ import absolute_import
import os

from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


# Frankfurt AWS workaround:
os.environ['S3_USE_SIGV4'] = 'True'
class S3Storage(S3BotoStorage):
    @property
    def connection(self):
        if self._connection is None:
            self._connection = self.connection_class(
                self.access_key,
                self.secret_key,
                calling_format=self.calling_format,
                host='s3.eu-central-1.amazonaws.com'
            )
        return self._connection


class StaticStorage(S3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Storage):
    location = settings.MEDIAFILES_LOCATION
