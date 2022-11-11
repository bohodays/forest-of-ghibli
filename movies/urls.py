from django.urls import path
from . import views


app_name='movies'
urlpatterns = [
    path('main', views.main, name='main'),
    path('intro', views.intro, name='intro'),
    path('detail/<int:pk>', views.detail, name='detail'),
]