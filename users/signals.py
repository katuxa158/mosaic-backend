from django.dispatch import receiver
from django.db.models.signals import post_migrate
from django.contrib.auth.signals import user_logged_in, user_logged_out

from users.models import Role


@receiver(post_migrate)
def create_default_roles(sender, **kwargs):

    roles = ['User', 'Administrator']
    for role in roles:
        Role.objects.get_or_create(name=role)

@receiver(user_logged_in)
def set_online(sender, user, request, **kwargs):
    user.is_online = True
    user.save(update_fields=['is_online'])


@receiver(user_logged_out)
def set_offline(sender, user, request, **kwargs):
    user.is_online = False
    user.save(update_fields=['is_online'])