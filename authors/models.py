from django.db import models

# authors/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
