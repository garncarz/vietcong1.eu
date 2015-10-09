from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.ServerListView.as_view(),
        name='server_list'),
    url(r'^(?P<ip>[\d.]+):(?P<port>\d+)$',
        views.ServerDetailView.as_view(),
        name='server_detail'),
    url(r'^players$',
        views.PlayerListView.as_view(),
        name='player_list'),
    url(r'^map/(?P<pk>\d+)$',
        views.MapDetailView.as_view(),
        name='map_detail'),
]
