from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from core import views
from django.contrib.sitemaps.views import sitemap
from .views import StaticViewSitemap
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

sitemaps = {
    'static': StaticViewSitemap,
}

admin.site.site_header = "GAMESHOP ADMIN"
admin.site.site_title = "Gameshop Admin Portal"
admin.site.index_title = "Welcome to Gameshop Admin Portal"

urlpatterns = [
    path('gameshop-admin-portal/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
    path('favicon.ico/', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.png'), permanent=True)),
    path("ads.txt/", RedirectView.as_view(url=staticfiles_storage.url("ads.txt"))),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]

if settings:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.handler404
handler500 = views.handler500
