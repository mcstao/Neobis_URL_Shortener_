import uuid
from django.db import models


class Url(models.Model):
    full_url = models.URLField(max_length=1000, verbose_name="Полная ссылка")
    short_url = models.CharField(max_length=30, unique=True, verbose_name="Короткая ссылка", blank=True)

    def __str__(self):
        return self.full_url, self.short_url

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = str(uuid.uuid4())[:7]
        super().save(*args, **kwargs)
