from django.shortcuts import render,get_object_or_404
from .serializers import ScrapPostSerializer,ScrapSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Scrap
from courses.models import Course

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def scrap_access(request):
    if request.method == 'POST':
        serializer = ScrapPostSerializer(data=request.data)
        serializer.is_valid()
        scrap_data = serializer.validated_data
        course = Course.objects.get(pk=scrap_data['course'])
        scrap=Scrap.objects.create(course=course, cousUser=request.user)
        serializer = ScrapSerializer(instance=scrap)
        return Response(serializer.data)
    elif request.method == 'GET':
        queryset = Scrap.objects.filter(cousUser=request.user)
        serializer = ScrapSerializer(queryset,many=True)
        return Response(serializer.data)

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def scrap_access_one(request,pk):
    if request.method == 'GET':
        scraps = Scrap.objects.all()
        scrap = get_object_or_404(scraps,pk=pk)
        serializer = ScrapSerializer(scrap)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        scraps = Scrap.objects.all()
        scrap = get_object_or_404(scraps,pk=pk)
        scrap.delete()
        return Response(status=204)