from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.TextField()
    poster_path = models.TextField()
    vote_average = models.TextField()
    director = models.TextField()
    wise_saying = models.TextField()

    def __str__(self):
        return f'{ self.title }'


class Comment(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='comments')
    