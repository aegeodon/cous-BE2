from rest_framework import serializers
from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tagName']