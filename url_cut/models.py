# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from base.models import BaseModel


class ShortenUrl(BaseModel):
    def __str__(self):
        return str(self.id)

    id = models.AutoField(primary_key=True)
    short_url = models.CharField(max_length=255, db_index=True)
    mask = models.PositiveIntegerField(default=0, db_index=True)
    long_url = models.TextField()
