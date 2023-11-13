from django.urls import path
from .views import UrlListCreateView, UrlRetrieveView


urlpatterns = [
    path('', UrlListCreateView.as_view()),
    path('<str:short_url>/', UrlRetrieveView.as_view()),
]