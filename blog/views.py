from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post, Category, Tag
from .forms import CommentForm, RegisterForm


def home(request):
    posts = Post.objects.filter(published=True).order_by('-created')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/home.html', {'page_obj': page_obj})

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

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, published=True)
    return render(request, 'blog/category.html', {
        'category': category,
        'posts': posts
    })

def tagged_posts(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag, published=True).order_by('-created')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/tagged_posts.html', {
        'tag': tag,
        'page_obj': page_obj
    })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.wants_newsletter = form.cleaned_data['wants_newsletter']
            user.profile.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('account_deleted')
    return render(request, 'blog/delete_account.html')

def terms_view(request):
    return render(request, 'blog/terms.html')

def privacy_view(request):
    return render(request, 'blog/privacy.html')
