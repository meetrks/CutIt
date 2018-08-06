import time

from django.conf import settings as cfg
from django.core.validators import URLValidator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ShortenUrl


class ShortenUrlView(ListAPIView):
    def get(self, request):
        try:
            return render(request, 'index.html')
        except Exception as e:
            print e
            return render(request, 'error_page.html')


class EncodeUrl(APIView):
    throttle_scope = 'encode_url'

    def get(self, request):
        url = request.query_params.get('url')
        if not url:
            return Response({"detail": "Please provide url."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            url_validator = URLValidator()
            url_validator(url)
        except:
            return Response({"detail": "Please enter a valid url"}, status=status.HTTP_400_BAD_REQUEST)

        short_id = ShortenUrl.objects.create(long_url=url)
        time_now = int(time.time())
        mask = int(short_id.pk) + time_now
        short_id.mask = mask
        encoding = ""
        while mask:
            mask, rem = divmod(mask, cfg.BASE62_LEN)
            encoding = cfg.BASE62[rem] + encoding
        short_url = encoding
        short_id.short_url = short_url
        short_id.save()
        res = {
            'shortUrl': cfg.BASE_URL + short_url,
            'longUrl': url,
        }
        return Response(res, status=status.HTTP_200_OK)


class DecodeUrl(ListAPIView):
    def get(self, request, id):
        try:
            text = id
            num = 0
            for char in text:
                num = num * cfg.BASE62_LEN + cfg.BASE62_DICT[char]
            url = ShortenUrl.objects.get(mask=num, short_url=id)
            return HttpResponseRedirect(url.long_url)
        except Exception as e:
            print(e)
            return Response({"detail": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
