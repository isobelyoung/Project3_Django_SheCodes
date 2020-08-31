from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # this is where to add custom fields eg. add address, fave colour 
    first_name = models.TextField(max_length=20, blank=False)
    last_name = models.TextField(max_length=20, blank=True)
    

    def __str__(self):
        return self.username