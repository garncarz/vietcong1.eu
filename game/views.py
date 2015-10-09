from django.views import generic

from . import models


class ServerListView(generic.ListView):
    model = models.Server

    def get_queryset(self):
        return (super().get_queryset()
            .select_related('map', 'mode')
            .filter(online=True)
            .all())


class ServerDetailView(generic.DetailView):
    model = models.Server


class PlayerListView(generic.ListView):
    model = models.Player

    def get_queryset(self):
        return (super().get_queryset()
            .select_related('server')
            .filter(online=True, server__online=True)
            .all())


class MapDetailView(generic.DetailView):
    model = models.Map
