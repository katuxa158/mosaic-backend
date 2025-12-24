from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=256)
    likes_count = models.PositiveIntegerField(default=0)
    dislikes_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)