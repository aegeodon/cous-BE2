from rest_framework import serializers
from .models import Scrap

class ScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrap
        fields = '__all__'

class ScrapPostSerializer(serializers.Serializer):
    course = serializers.IntegerField()
