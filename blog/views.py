from django.shortcuts import render, redirect

from blog.models import Post
from .forms import PostModelForm, PostUpdateForm, CommentForm


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


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('post_detail', pk=post.id)
    else:
        c_form = CommentForm()
    context = {
        'post': post,
        'c_form': c_form,
    }
    return render(request, 'blog/post_detail.html', context)


def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'blog/post_edit.html', context)


def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('home')

    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context=context)
