from django.db import models
from django.conf import settings

from posts.models import Post


class Reaction(models.Model):
    LIKE = 'LIKE'
    DISLIKE = 'DISLIKE'

    TYPES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    type = models.CharField(max_length=7, choices=TYPES)

    class Meta:
        unique_together = ('user', 'post')
