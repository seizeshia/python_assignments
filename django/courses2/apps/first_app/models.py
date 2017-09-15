from django.db import models


class Courses(models.Model):
    name= models.CharField(max_length=50)
    description= models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)
