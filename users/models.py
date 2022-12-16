from django.db import models
from django.contrib.auth.models import AbstractUser


class UserCustom(AbstractUser):
    image = models.ImageField(upload_to='users/', null=True, blank=True)