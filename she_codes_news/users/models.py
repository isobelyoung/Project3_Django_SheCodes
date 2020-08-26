from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # this is where to add custom fields eg. add address, fave colour 
    pass

    def __str__(self):
        return self.username