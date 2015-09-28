from django.views import generic

from . import models


class ServerListView(generic.ListView):
    model = models.Server
