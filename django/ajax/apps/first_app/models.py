# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PostsManager(models.Manager):
    def posting(self, data):
        Posts.objects.create(post=data['currentpost'])
        return 'apples'

class Posts(models.Model):
    post=models.CharField(max_length=255)
    created_at=models.DateField(auto_now_add=True)
    objects=PostsManager()

# Create your models here.
