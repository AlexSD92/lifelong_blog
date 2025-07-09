from django import forms
from .models import Comment, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import admin

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    wants_newsletter = forms.BooleanField(
        required=False,
        label="I'd like to receive email updates and newsletters."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'wants_newsletter']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'category', 'image', 'body', 'published']

# Or in admin:
class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'body', 'image', ...)

