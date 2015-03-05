from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fenavist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'institucional.views.home', name='home'),
    url(r'^institucional/sobre$', 'institucional.views.sobre', name='sobre'),
    url(r'^institucional/equipe$', 'institucional.views.equipe', name='equipe'),
    url(r'^institucional/parcerias$', 'institucional.views.parcerias', name='parcerias'),
    url(r'^institucional/sindicatos$', 'institucional.views.sindicatos', name='sindicatos'),

    url(r'^agenda/eventos$', 'agenda.views.eventos', name='eventos'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)