from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # this is where to add custom fields eg. add address, fave colour 
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=True)
    profile_img = models.ImageField(upload_to='images/', null=True, blank=True, default='users/static/users/images/profile_default.gif')
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)

    def __str__(self):
        return self.first_name