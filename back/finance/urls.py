from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('exchange_rate/', views.exchange_rate),
]