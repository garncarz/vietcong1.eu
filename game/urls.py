from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ServerListView.as_view(), name='server_list'),
]
