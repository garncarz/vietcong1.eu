import random

from faker import Factory
from faker.providers import BaseProvider
from faker.providers.date_time import Provider as DTProvider

faker = Factory.create()


class ExtraProviderMeta(type):
    def __init__(cls, name, bases, nmspc):
        super().__init__(name, bases, nmspc)
        cls.select_countries()

    @classmethod
    def select_countries(cls):
        countries = DTProvider.countries
        include = lambda cond: list(filter(lambda c: cond(c), countries))

        countries = (
            include(lambda c: c['continent'] in ['Europe', 'Oceania']) +
            include(lambda c: 'America' in c['continent']) +
            include(lambda c: c['code'] in ['IL', 'JP', 'MN', 'NP', 'BT', 'MM',
                                            'AM', 'TH', 'VN', 'KR', 'KH', 'LA'])
        )
        countries = filter(lambda c: c['code'] not in ['AL', 'XK'], countries)

        cls.countries = list(countries)


class ExtraProvider(BaseProvider, metaclass=ExtraProviderMeta):

    @classmethod
    def country(cls):
        return random.choice(cls.countries)


faker.add_provider(ExtraProvider)
