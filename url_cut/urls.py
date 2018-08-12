from django.conf.urls import url

from .views import *

urlpatterns = [
    url('^$', ShortenUrlView.as_view(), name='shorten_url_view'),
    url('^encode_url/$', EncodeUrl.as_view(), name='encode_url'),
    url('^(?P<id>[a-zA-Z0-9]{7,8})/$', DecodeUrl.as_view(), name='decode_url')
]
