from django.db import models
from django.contrib.auth.models import AbstractUser


def accounts_image_path(instance, filename):
    print(instance)
    return f'accounts/{filename}'
# Create your models here.
class User(AbstractUser):
    nickName = models.CharField(max_length =20, unique = True, blank=False)
    profileImg = models.ImageField(blank=True, upload_to=accounts_image_path)
    GBTI = models.TextField(blank=True)
    
