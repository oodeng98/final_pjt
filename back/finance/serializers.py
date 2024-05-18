from rest_framework import serializers
from .models import Exchangerate
from .models import Product

class ExchangerateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exchangerate
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'