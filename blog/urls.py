from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('tag/<slug:slug>/', views.tagged_posts, name='tagged_posts'),
    path('register/', views.register, name='register'), 
    path('delete-account/', views.delete_account, name='delete_account'),
    path('account-deleted/', TemplateView.as_view(template_name='blog/account_deleted.html'), name='account_deleted'),
    path('terms/', views.terms_view, name='terms'),
    path('privacy/', views.privacy_view, name='privacy'),
]
