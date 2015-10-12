from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(pattern_name='game:server_list',
                                    permanent=False)),
] + i18n_patterns(
    url(r'^', include('game.urls', namespace='game')),
)
