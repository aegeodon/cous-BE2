from django.db import models
from courses.models import Course

# Create your models here.

class Tag(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tagName = models.TextField()