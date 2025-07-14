from django import forms
from .models import Comment, Post
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

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

class CustomPasswordResetForm(PasswordResetForm):
    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        # 🔒 Hardcoded subject override
        subject = "Reset Your Password – WhatTheVolt"
        
        # Render plain-text email body
        body = render_to_string(email_template_name, context)
        
        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        
        # Optionally add HTML email (if you create one)
        if html_email_template_name:
            html_email = render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, "text/html")
        
        email_message.send()


