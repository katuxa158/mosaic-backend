from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from posts.models import Post

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=Post)
def increment_posts_count(sender, instance, created, **kwargs):
    if created:
        user = instance.author
        user.posts_count += 1
        user.save(update_fields=['posts_count'])


@receiver(post_delete, sender=Post)
def decrement_posts_count(sender, instance, **kwargs):
    user = instance.author
    if user.posts_count > 0:
        user.posts_count -= 1
        user.save(update_fields=['posts_count'])