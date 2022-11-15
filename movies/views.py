from django.shortcuts import render, get_list_or_404,redirect
from .models import Movie, Comment, Director
from .forms import CommentForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods

from django.http import JsonResponse

# Create your views here.
def main(request):
    movies = get_list_or_404(Movie)
    context = {
        'movies': movies,
    }
    return render(request,'movies/main.html', context)


def intro(request):
    return render(request, 'movies/intro.html')


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    #  댓글 작성을 하는 폼 생성
    comment_form = CommentForm()
    # 댓글 목록
    comments = movie.comments.all()
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request,'movies/detail.html',context)

# 댓글 생성하는 함수
@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
        return redirect('movies:detail',movie.pk)
    return redirect('accounts:login')


# 댓글 삭제
def comments_delete(request, movie_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:detail',movie_pk)


# 댓글 수정
@login_required
@require_http_methods(['GET','POST'])
def comments_update(request,movie_pk,comment_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment = Comment.objects.get(pk=comment_pk)
    # print('\n\n',comment.content,'\n')

    if request.user == comment.user:
        # if request.method =='POST':
        comment_form = CommentForm(data=request.POST, instance=comment)
        # print('\n\n',comment_form.instance.content,'\n')
        
        if comment_form.is_valid():
            comment_form.save()
            print('\n\n',comment_form.instance.content,'\n')
            return redirect('movies:detail',movie.pk)
        else:
            comment_form = CommentForm(instance=comment)
        context={
            'movie':movie,
            'comment_form':comment_form,
            'comment':comment,
        }
    return render(request,'movies/comments_update.html', context)
    # movie = Movie.objects.get(pk=movie_pk)
    # comment = Comment.objects.get(pk=comment_pk)
    # if request.user == comment.user:
    #     if request.method =="POST":
    #         form = CommentForm(request.POST, instance = comment)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('movies:detail',movie.pk, comment.pk)
    #     else:
    #         form = CommentForm(instance = comment)
    # else:
    #     return redirect('accounts:main')
            
# 좋아요
def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)

        if movie.like_users.filter(pk=request.user.pk).exist():
            movie.like_users.remove(request.user)
            is_liked=False
        else:
            movie.like_users.add(request.user)
            is_liked=True
        context = {
            'is_liked':is_liked,
        }
        return JsonResponse(context)
    return redirect('accounts:login')

def films(request):
    movies = get_list_or_404(Movie)
    context = {
        'movies': movies,
    }
    return render(request, 'movies/films.html', context)


def directors(request):
    directors = get_list_or_404(Director)
    tmp = []
    for director in directors:
        tmp.append((director.name, director.profileImg))
    tmp = list(set(tmp))
    directors = {}
    for i in tmp:
        directors[i[0]] = i[1]
    context = {
        'directors': directors,
    }
    return render(request, 'movies/directors.html', context)


def directors_detail(request, name):
    movies = get_list_or_404(Movie)
    directors = get_list_or_404(Director)

    # 클릭된 감독의 영화 데이터를 딕셔너리 형태로 저장
    selected_movies = []
    for movie in movies:
        if movie.director == name:
            tmp = {
                'id': movie.id,
                'title': movie.title,
                'overview': movie.overview,
                'release_date': movie.release_date,
                'poster_path': movie.poster_path,
                'vote_average': movie.vote_average,
                'director': movie.director,
                'wise_saying': movie.wise_saying
            }
            selected_movies.append(tmp)

    # 클릭된 영화 감독의 정보를 딕셔너리 형태로 저장
    for director in directors:
        if director.name == name:
            selected_director = {
                'id': director.id,
                'name': director.name,
                'profileImg': director.profileImg,
                'wise_saying': director.wise_saying
            }
    context = {
        'selected_movies': selected_movies,
        'selected_director': selected_director,
    }
    return render(request, 'movies/directors_detail.html', context)
