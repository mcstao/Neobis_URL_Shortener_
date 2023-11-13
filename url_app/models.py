from django.db import models
import requests
import uuid
from bs4 import BeautifulSoup


class Url(models.Model):
    full_url = models.URLField(max_length=1000, verbose_name="Полная ссылка")
    short_url = models.CharField(max_length=30, unique=True, verbose_name="Короткая ссылка", blank=True)
    title_url = models.CharField(max_length=100, blank=True, verbose_name='Описание ссылки')

    def __str__(self):
        return self.full_url, self.short_url, self.title_url

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = str(uuid.uuid4())[:7]
        html_info = requests.get(self.full_url)
        soup = BeautifulSoup(html_info.content, 'html.parser')
        title = soup.find('title')
        self.title_url = title.text
        super().save(*args, **kwargs)
