from django.shortcuts import render, get_list_or_404,redirect
from .models import Movie, Comment
from .forms import CommentForm

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
def comments_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.save()
    return redirect('movies:detail',movie.pk)


# 댓글 삭제
def comments_delete(request, movie_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.object.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:detail',movie_pk)
