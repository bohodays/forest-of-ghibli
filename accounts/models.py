from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

def accounts_image_path(instance, filename):
    print(instance)
    return f'accounts/{filename}'
# Create your models here.
class User(AbstractUser):
    nickName = models.CharField(max_length =20, unique = True, blank=False)
    profileImg = models.ImageField(blank=True, upload_to=accounts_image_path)
    GBTI = models.TextField(blank=True)
    quiz_rank = models.TextField(blank=True)
    movie_title = models.CharField(max_length=20, blank=True)
    movie_poster = models.TextField(blank=True)

