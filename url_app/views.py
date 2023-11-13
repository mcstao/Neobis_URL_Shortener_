from django.shortcuts import redirect
from rest_framework import generics
from .models import Url
from .serializers import UrlSerializer
from django.http import Http404


class UrlListCreateView(generics.ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class UrlRetrieveView(generics.RetrieveAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    lookup_field = 'short_url'

    def retrieve(self, request, *args, **kwargs):
        try:
            new_url = self.get_object()
            return redirect(new_url.full_url)
        except Url.DoesNotExist:
            raise Http404


