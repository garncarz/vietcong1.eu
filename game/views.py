from django.views import generic

from . import models


class ServerListView(generic.ListView):
    model = models.Server

    def get_queryset(self):
        return super().get_queryset().filter(online=True)


class ServerDetailView(generic.DetailView):
    model = models.Server
