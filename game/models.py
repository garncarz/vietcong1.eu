from django.db import models


class Mode(models.Model):
    name = models.CharField(max_length=256, unique=True)


class Map(models.Model):
    name = models.CharField(max_length=256, unique=True)
    modes = models.ManyToManyField(Mode)


class Server(models.Model):
    ip = models.GenericIPAddressField()
    infoport = models.PositiveSmallIntegerField()
    port = models.PositiveSmallIntegerField()

    name = models.CharField(max_length=256)
    map = models.ForeignKey(Map)
    mode = models.ForeignKey(Mode)

    country = models.CharField(max_length=2, null=True)
    country_name = models.CharField(max_length=50, null=True)

    version = models.CharField(max_length=4)
    hradba = models.CharField(max_length=4, null=True)
    numplayers = models.PositiveSmallIntegerField()
    maxplayers = models.PositiveSmallIntegerField()

    password = models.BooleanField(default=False)
    dedic = models.BooleanField(default=False)
    vietnam = models.BooleanField(default=False)

    online = models.BooleanField(default=True)
    online_since = models.DateTimeField(auto_now_add=True)
    offline_since = models.DateTimeField(null=True)


class Player(models.Model):
    name = models.CharField(max_length=256)
    ping = models.PositiveSmallIntegerField()
    frags = models.PositiveSmallIntegerField()

    server = models.ForeignKey(Server)

    online = models.BooleanField(default=True)
    online_since = models.DateTimeField(auto_now_add=True)
