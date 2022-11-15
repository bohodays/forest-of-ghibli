from django.urls import path
from . import views


app_name='movies'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('intro/', views.intro, name='intro'),
<<<<<<< HEAD
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
=======
    path('films/', views.films, name='films'),
    path('directors/', views.directors, name='directors'),
>>>>>>> d92d3bed3ea08175cce135c9482efe4516934c9d
]