from django.contrib import messages
from django.shortcuts import redirect
from django.views import generic
from rest_framework import viewsets

from . import forms
from . import models
from . import serializers


class ServerListView(generic.ListView):
    model = models.Server

    def get_queryset(self):
        return (super().get_queryset()
            .select_related('map', 'mode')
            .filter(online=True)
            .all())


class ServerViewSet(viewsets.ModelViewSet):
    queryset = models.Server.objects.all().order_by('name')
    serializer_class = serializers.ServerSerializer


class ServerDetailView(generic.DetailView):
    model = models.Server

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        return queryset.get(ip=self.kwargs['ip'], port=self.kwargs['port'])


class PlayerListView(generic.ListView):
    model = models.Player

    def get_queryset(self):
        return (super().get_queryset()
            .select_related('server')
            .filter(online=True, server__online=True)
            .all())


class MapDetailView(generic.DetailView):
    model = models.Map


class MapImageUploadView(generic.FormView):
    template_name = 'game/mapimage_upload.html'
    form_class = forms.MapImageForm

    def get_map(self):
        return models.Map.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['map'] = self.get_map()
        return context

    def form_valid(self, form):
        map_image = form.save(commit=False)
        map_image.map = self.get_map()
        map_image.save()
        messages.success(self.request, 'The picture has been uploaded.')
        return redirect(map_image.map)
