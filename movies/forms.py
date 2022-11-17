from .models import Movie, Comment
from django import forms

class CommentForm(forms.ModelForm):
    # content = forms.CharField(
    #     widget=forms.Textarea(attrs={
    #         'cols': 80,
    #         })
    # )


    class Meta:
        model= Comment
        fields= ('content','movie_rate','like_users')



