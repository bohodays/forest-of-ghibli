from django.urls import path
from . import views


app_name='movies'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('intro/', views.intro, name='intro'),
    path('films/', views.films, name='films'),
    path('directors/', views.directors, name='directors'),
]