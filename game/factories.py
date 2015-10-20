from datetime import datetime, timedelta
import random

from factory import lazy_attribute, post_generation
from factory.django import DjangoModelFactory
from faker import Factory
from faker.providers.address import Provider as AddressProvider

from . import models

faker = Factory.create()
lazy = lambda call: lazy_attribute(lambda obj: call())
lazy_bool = lazy(lambda: random.choice([True, False]))
rand_obj = lambda model: model.objects.order_by('?').first()
lazy_obj = lambda model: lazy(lambda: model.objects.order_by('?').first())
lazy_subobj = lambda get_model: \
    lazy_attribute(lambda obj: get_model(obj).order_by('?').first())
lazy_choice = lambda choices: lazy(lambda: random.choice(choices))
lazy_randint = lambda min, max: lazy(lambda: random.randint(min, max))


class Mode(DjangoModelFactory):
    class Meta:
        model = models.Mode
        django_get_or_create = ['name']

    name = lazy(faker.word)


class Map(DjangoModelFactory):
    class Meta:
        model = models.Map
        django_get_or_create = ['name']

    name = lazy(lambda: faker.sentence(2))

    @post_generation
    def modes(self, create, extracted, **kwargs):
        for _ in range(random.randint(1, 5)):
            self.modes.add(rand_obj(models.Mode))


class Server(DjangoModelFactory):
    class Meta:
        model = models.Server
        django_get_or_create = ['ip', 'port']

    ip = lazy(faker.ipv4)
    infoport = lazy_randint(15425, 15430)
    port = lazy_randint(5425, 5430)

    name = lazy(lambda: faker.sentence(2))
    map = lazy_obj(models.Map)
    mode = lazy_subobj(lambda obj: obj.map.modes)

    @post_generation
    def country(self, create, extracted, **kwargs):
        i = random.randint(0, len(AddressProvider.countries) - 1)
        self.country = AddressProvider.country_codes[i]
        self.country_name = AddressProvider.countries[i]
        self.save()

    version = lazy_choice(['1.60', '1.01'])
    hradba = lazy_choice([None, '206'])
    maxplayers = lazy_randint(5, 20)

    @lazy_attribute
    def numplayers(self):
        return random.randint(0, self.maxplayers)

    @post_generation
    def players(self, create, extracted, **kwargs):
        [Player(server=self) for _ in range(self.numplayers)]

    password = lazy_bool
    dedic = lazy_bool
    vietnam = lazy_bool

    online = True
    online_since = lazy(
        lambda: datetime.now() - timedelta(days=random.randint(0,2),
                                           hours=random.randint(0, 24))
        )


class Player(DjangoModelFactory):
    class Meta:
        model = models.Player

    name = lazy(faker.name)
    ping = lazy_randint(8, 200)
    frags = lazy_randint(-5, 150)

    server = lazy_obj(models.Server)

    online = True
    online_since = lazy(
        lambda: datetime.now() - timedelta(hours=random.randint(0, 7),
                                           minutes=random.randint(0, 60))
        )
