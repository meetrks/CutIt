from django.conf import settings as cfg
from django.core.validators import URLValidator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.crypto import get_random_string
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
            return render(request, 'error_page.html')


class EncodeUrl(APIView):
    throttle_scope = 'encode_url'

    def get(self, request):
        url = request.query_params.get('url')
        if not url:
            return Response({"detail": "Please provide url"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            url_validator = URLValidator()
            url_validator(url)
        except:
            return Response({"detail": "Please enter a valid url"}, status=status.HTTP_400_BAD_REQUEST)

        short_id = get_random_string(length=7, allowed_chars=cfg.BASE62)
        ShortenUrl.objects.create(id=short_id, long_url=url)

        res = {
            'shortUrl': cfg.BASE_URL + short_id,
            'longUrl': url,
        }
        return Response(res, status=status.HTTP_200_OK)


class DecodeUrl(ListAPIView):
    def get(self, request, id):
        try:
            short_obj = ShortenUrl.objects.get(pk=id)
            short_obj.hit_count += 1
            short_obj.save()
            return HttpResponseRedirect(short_obj.long_url)
        except Exception as e:
            return Response({"detail": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
