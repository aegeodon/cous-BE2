from rest_framework import serializers

from .models import Course
from places.serializers import PlaceSerializer, PlaceCreateSerializer
from tags.serializers import TagSerializer, TagCreateSerializer

class CourseSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(many=True)
    tag = TagSerializer(many=True)
    class Meta:
        model = Course
        fields = ['area','description','content','place','tag']
        
class CoursePostSerializer(serializers.ModelSerializer):
    places = PlaceCreateSerializer(many=True)
    tags = TagCreateSerializer(many=True)
    
    class Meta:
        model = Course
        fields = ['area', 'description', 'content', 'places', 'tags']
    
class CourseResponseSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, source='place_set')
    tags = TagSerializer(many=True, source='tag_set')
    
    class Meta:
        model = Course
        fields = ['id', 'cousUser', 'area', 'description', 'content', 'places', 'tags']