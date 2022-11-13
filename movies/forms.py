from .models import Movie, Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields= ('content','movie_rate',)


