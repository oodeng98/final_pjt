from rest_framework import serializers
from .models import Exchangerate


class ExchangerateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exchangerate
        fields = '__all__'