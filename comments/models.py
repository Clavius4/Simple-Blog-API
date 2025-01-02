from django.db import models

from posts.models import Post


# Create your models here.

class Comments(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment on {self.post.title}'

    # @property
    # def author(self):
    #     return self.author.username

