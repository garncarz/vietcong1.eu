from django.conf.urls import url, include
from rest_framework import routers

from . import views

api_router = routers.DefaultRouter()
api_router.register(r'server', views.ServerViewSet)

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
    url(r'^map/(?P<pk>\d+)/upload-img$',
        views.MapImageUploadView.as_view(),
        name='map_upload_img'),
    url(r'^api/', include(api_router.urls, namespace='api')),
]
