from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('exchange_rate/', views.exchange_rate),
    path('products/save/', views.save),
    path('products/get_product/', views.get_product),
]