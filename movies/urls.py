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
    path('films/', views.films, name='films'),
    path('directors/', views.directors, name='directors'),
    path('directors/<str:name>/', views.directors_detail, name='directors_detail'),
    path('GBTI/<int:user_pk>/', views.GBTI, name='GBTI'),
    path('GBTI/<int:user_pk>/create', views.GBTI_create, name='GBTI_create'),
    path('GBTI_result/<int:user_pk>/', views.GBTI_result, name="GBTI_result"),
    path('quiz/<int:user_pk>/', views.quiz, name='quiz'),
    path('quiz/<int:user_pk>/create', views.quiz_create, name='quiz_create'),
    path('quiz_result/<int:user_pk>/', views.quiz_result, name='quiz_result'),
]