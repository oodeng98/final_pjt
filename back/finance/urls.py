from django.urls import path
from . import views

urlpatterns = [
    path('exchange_rate/', views.exchange_rate),
    path('products/save/', views.save),
    path('products/get_product/', views.get_product),
    path('products/subscribe/', views.subscribe),
]