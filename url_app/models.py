import uuid
from django.db import models


class Url(models.Model):
    full_url = models.URLField(max_length=1000, verbose_name="Полная ссылка")
    short_url = models.CharField(max_length=30, unique=True, verbose_name="Короткая ссылка", blank=True)


