from .models import Movie, Comment
from django import forms
from django.contrib.auth import get_user_model

class CommentForm(forms.ModelForm):
    
    class Meta:
        model= Comment
        fields= ('content','movie_rate',)


class GBTIForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('GBTI',)
        # fields = '__all__'


class quizForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('quiz_rank',)