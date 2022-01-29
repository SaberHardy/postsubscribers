from django.shortcuts import render, redirect

from blog.models import Post
from .forms import PostModelForm


def home(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = PostModelForm()
    context = {
        'posts': posts,
        'form': form
    }

    return render(request, 'blog/index.html', context=context)


def post_detail(request, id):
    post = Post.objects.get(pk=id)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)
