from django.conf.urls import url, include
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/st/logo/logo_36x36.png', permanent=True)
robots_view = RedirectView.as_view(url='/st/robots.txt', permanent=True)
sitemap_view = RedirectView.as_view(url='/st/sitemap.xml', permanent=True)

urlpatterns = [
    url('', include('url_cut.urls')),
    url(r'^favicon\.ico$', favicon_view),
    url(r'^robots.txt$', robots_view),
    url(r'^sitemap.xml$', sitemap_view),
]
