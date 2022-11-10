from django.shortcuts import render, get_list_or_404
from .models import Movie

# Create your views here.
def main(request):
    movies = get_list_or_404(Movie)
    context = {
        'movies': movies,
    }
    return render(request,'movies/main.html', context)

def intro(request):
    return render(request, 'movies/intro.html')