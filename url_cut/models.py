# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from base.models import BaseModel


class ShortenUrl(BaseModel):
    def __str__(self):
        return str(self.id)

    id = models.CharField(max_length=10, primary_key=True)
    expiration = models.CharField(max_length=255, null=True, blank=True)
    long_url = models.TextField()
    hit_count = models.PositiveIntegerField(default=0)
