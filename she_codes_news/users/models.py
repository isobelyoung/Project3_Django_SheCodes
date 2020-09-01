from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # this is where to add custom fields eg. add address, fave colour 
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=True)
    profile_img = models.ImageField(upload_to='images/', null=True, blank=True, default='/media/images/default_story.jpg')
    

    def __str__(self):
        return self.username