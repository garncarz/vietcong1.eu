from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.ServerListView.as_view(),
        name='server_list'),
    url(r'^(?P<pk>\d+)$',  # TODO ip:port
        views.ServerDetailView.as_view(),
        name='server_detail'),
    url(r'^players$',
        views.PlayerListView.as_view(),
        name='player_list'),
]
