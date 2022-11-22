from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm, CustomUserChangeForm
from movies.models import Character, Movie
from django.http.response import JsonResponse

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:main')
    if request.method =="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:main')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('movies:main')

# 회원가입
def signup(request):
    if request.method=="POST":
        # 프로필 사진을 따로 받아주기위해 인자 추가
        form = CustomUserCreationForm(request.POST,request.FILES)
        print('request\n', request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('movies:main')
    else:
        form = CustomUserCreationForm(request.FILES)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('movies:main')

# 회원정보 수정
def update(request):
    if request.method =="POST":
        form = CustomUserChangeForm(request.POST, request.FILES,instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('movies:main')
    else:
        form = CustomUserChangeForm(request.FILES, instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html',context)


def change_password(request):
    if request.method =="POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('movies:main')
    form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/change_password.html',context)


# 프로필 페이지
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    movies = Movie.objects.all()
    bookmark_movies = []
    context = {}
    
    for movie in movies:
        if movie.bookmark.filter(bookmark_movie= movie.pk).exists() and movie.bookmark.filter(id = request.user.pk).exists():
            movie_dic = {
                'pk': movie.pk,
                'title' : movie.title,
                'overview': movie.overview,
                'release_date': movie.release_date,
                'poster_path': movie.poster_path,
                'vote_average': movie.vote_average,
                'director': movie.director,
                'backgroundImg': movie.backgroundImg,
                }
            bookmark_movies.append(movie_dic)
            context = {
                'bookmark_movies': bookmark_movies
            }
    if person.GBTI:
        character = Character.objects.get(MBTI=person.GBTI)
        context['person'] = person
        context['character'] = character
        return render(request, 'accounts/profile.html', context)
    else:
        context['person'] = person
        return render(request, 'accounts/profile.html', context)


    

# =======
# def profile(request):
    
#     movies = Movie.objects.all()
#     # print(type(movies))
#     bookmark_movie = []
#     index = 0
#     for movie in movies:
#         index += 1
#         if movie.bookmark.filter(bookmark_movie= movie.pk).exists() and movie.bookmark.filter(id = request.user.pk).exists():
#             # print(type(movie.title))
#             movie_dic = {
#                 'title' : movie.title,
#                 'poster': movie.poster_path,
#                  }
#             # print(json.dumps(movie_dic))
#             bookmark_movie.append(movie_dic)
#     context = {
#     'bookmark_movie':bookmark_movie
#     }
#     return render(request, 'accounts/profile.html',context)
# >>>>>>> 393215e34583449c3f219875f8de46a38224f706
