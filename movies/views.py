from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'movies/main.html')

def intro(request):
    return render(request, 'movies/intro.html')