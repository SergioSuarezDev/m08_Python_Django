from django.db import models

# Create your models here.

import datetime

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    text = models.TextField()
    image = models.URLField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    publication_date = models.DateTimeField(default=datetime.datetime.now)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.title

