from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length=255)
    weight = models.IntegerField(blank=True, null=True)
    prices = models.IntegerField()
    cost = models.IntegerField()
    category = models.CharField(max_length=50)

# Create your models here.
