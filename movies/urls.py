from django.urls import path
from . import views


app_name='movies'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('intro/', views.intro, name='intro'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:movie_pk>/comments/<int:comment_pk>/update/', views.comments_update, name='comments_update'),
    path('<int:movie_pk>/comments/<int:comment_pk>/likes/', views.comments_likes, name='comments_likes'),
    # 


    path('films/', views.films, name='films'),
    path('directors/', views.directors, name='directors'),
    path('directors/<str:name>/', views.directors_detail, name='directors_detail'),

]