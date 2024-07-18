from django.db import models
from courses.models import Course

# Create your models here.

class Place(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    address = models.TextField()