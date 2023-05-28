from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class custom_user(AbstractUser):
    USERS =[
        ('admin', 'Administrator'),
        ('user', 'Executive'),
        ]
    phone = models.CharField(max_length=15, null=True)
    profile_picture = models.ImageField(upload_to='profile')
    user_type = models.CharField(choices=USERS, default='admin', max_length=15)