from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    full_name = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    is_online = models.BooleanField(default=False)
    posts_count = models.PositiveIntegerField(default=0)