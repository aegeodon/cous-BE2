from rest_framework import serializers
from .models import Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id','address']
        
class PlaceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['address']