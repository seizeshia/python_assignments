from django.db import models

class Books(models.Model):
    title= models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published_date= models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=30)
    in_print = models.BooleanField()

# Create your models here.
