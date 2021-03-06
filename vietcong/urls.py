from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(pattern_name='game:server_list',
                                    permanent=False),
               name='home'),
] + i18n_patterns(
    url(r'^faq', views.FAQView.as_view(), name='faq'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('game.urls', namespace='game')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
