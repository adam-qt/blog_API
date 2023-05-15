from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    text = models.TextField(blank=True, default='blanc text')
    owner = models.ForeignKey(
        'auth.User',
        related_name='posts',
        on_delete=models.CASCADE)
    objects = models.Manager()


    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['-created', 'title'])
        ]

    def __str__(self):
        return self.title


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    objects = models.Manager()

    class Meta:
        ordering = ['created']

