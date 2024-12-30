from datetime import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title