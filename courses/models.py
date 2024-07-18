from django.db import models
from coususers.models import CousUser

# Create your models here.

class Course(models.Model):
    cousUser = models.ForeignKey(CousUser, on_delete=models.CASCADE)
    area = models.TextField()
    description = models.TextField(max_length=100)
    content = models.TextField(null=False)