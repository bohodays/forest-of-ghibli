from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'movies/index.html')

def intro(request):
    return render(request, 'movies/intro.html')