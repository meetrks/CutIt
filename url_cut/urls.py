from django.conf import settings
from django.conf.urls import url
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

from .views import *

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

urlpatterns = [
    url('^$', ShortenUrlView.as_view(), name='shorten_url_view'),
    url('^encode_url/$', EncodeUrl.as_view(), name='encode_url'),
    url('^(?P<id>[a-zA-Z0-9]{7,8})/$', cache_page(CACHE_TTL)(DecodeUrl.as_view()), name='decode_url')
]
