from django.db import models
from django.conf import settings

# Create your models here.

class Director(models.Model):
    name = models.TextField()
    profileImg = models.TextField()


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
    content = models.TextField(max_length=500)  # 리뷰 필드
    movie_rate = models.IntegerField()      # 영화 평점
    # 참조할 영화. 영화 1 : 댓글 N 관계
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 댓글 마다 좋아요를 달기 위해 like 추가 Comment, User M:N 관계 라서 변수명 뒤에 s 붙임
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')




