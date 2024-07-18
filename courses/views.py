from django.shortcuts import render, get_object_or_404

import os
import base64
import json

import requests

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from coususers.models import CousUser
from courses.models import Course
from places.models import Place
from tags.models import Tag
from coususers.serializers import KakaoLoginRequestSerializer, CousUserPatchSerializer, CousUserResponseSerializer
from .serializers import CourseSerializer, CourseResponseSerializer, CoursePostSerializer

# Create your views here.

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def course_access(request):
    if request.method == 'POST':
        serializer = CoursePostSerializer(data=request.data)
        if serializer.is_valid():
            inputData = serializer.validated_data

            course = Course(
                description=inputData['description'],
                content=inputData['content'],
                area=inputData['area'],
                cousUser=request.user
            )
            course.save()

            for p in inputData['places']:
                Place(course=course, address=p['address']).save()
            for t in inputData['tags']:
                Tag(course=course, tagName=t['tagName']).save()

            resSerializer = CourseResponseSerializer(course)
            return Response(resSerializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'GET':
        query = request.GET.get("area", "")
        if query:
            queryset = Course.objects.filter(area=query)
            serializer = CourseResponseSerializer(queryset,many=True)
            return Response(serializer.data)
        query2 = request.GET.get("tag", "")
        if query2:
            tags = Tag.objects.filter(tagName=query2)
            if tags.exists():
                courses = tags.values_list('course', flat=True)
                queryset = Course.objects.filter(id__in=courses)
                serializer = CourseResponseSerializer(queryset,many=True)
                return Response(serializer.data)

        queryset = Course.objects.all()
        serializer = CourseResponseSerializer(queryset,many=True)
        return Response(serializer.data)
    

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def course_access_one(request, pk):
    if request.method == 'GET':
        course = get_object_or_404(Course,pk=pk)
        serializer = CourseResponseSerializer(course)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        course = get_object_or_404(Course,pk=pk) 
        course.delete()
        return Response(status=204)