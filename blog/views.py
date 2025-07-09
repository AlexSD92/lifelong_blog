from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from .forms import RegisterForm

def home(request):
    posts = Post.objects.filter(published=True).order_by('-created')
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, published=True)
    return render(request, 'blog/category.html', {'category': category, 'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    comments = post.comments.filter(approved=True)
    new_comment = None

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.user = request.user
                new_comment.post = post
                new_comment.save()
        else:
            form = CommentForm()
    else:
        form = None

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
        'new_comment': new_comment
    })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ auto-login
            return redirect('home')  # redirect after successful registration
    else:
        form = RegisterForm()
    
    return render(request, 'blog/register.html', {'form': form})

def terms_view(request):
    return render(request, 'blog/terms.html')

def privacy_view(request):
    return render(request, 'blog/privacy.html')


