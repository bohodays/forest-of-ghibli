from django.contrib import admin
from .models import Movie, Director, Comment, Character

# Register your models here.
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Comment)
admin.site.register(Character)