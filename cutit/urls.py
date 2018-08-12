from django.conf.urls import url, include
from django.views.generic.base import RedirectView

robots_view = RedirectView.as_view(url='/st/robots.txt', permanent=True)
sitemap_view = RedirectView.as_view(url='/st/sitemap.xml', permanent=True)

urlpatterns = [
    url('', include('url_cut.urls')),
    url(r'^robots.txt$', robots_view),
    url(r'^sitemap.xml$', sitemap_view),
]
