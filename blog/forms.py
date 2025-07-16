from django import forms
from .models import Comment, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import admin


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "slug", "category", "image", "body", "published"]


# Newsletter signup form – stores email, no email sent
class NewsletterSignupForm(forms.Form):
    email = forms.EmailField(label="Your email", required=True)


# Optional: still allow admin UI for posts
class PostAdmin(admin.ModelAdmin):
    fields = ("title", "body", "image", "published")
