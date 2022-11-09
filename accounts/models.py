from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickName = models.CharField(max_length =20, unique = True, blank=True)
    profileImg = models.ImageField(upload_to='',blank=True)
    
