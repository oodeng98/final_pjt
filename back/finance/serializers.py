from rest_framework import serializers
from .models import Exchangerate

class ExchangerateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exchangerate
        fields = '__all__'
from .models import Product

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
