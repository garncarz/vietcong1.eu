from rest_framework import serializers

from . import models


class ServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Server
        fields = ['name', 'ip']
