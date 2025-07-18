from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView
from blog.forms import CustomPasswordResetForm

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "accounts/password_reset/",
        auth_views.PasswordResetView.as_view(form_class=CustomPasswordResetForm),
        name="password_reset",
    ),
    path("register/", views.register, name="register"),
    path("terms/", views.terms_view, name="terms"),
    path("privacy/", views.privacy_view, name="privacy"),
    path("search/", views.post_search, name="post_search"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path("category/<slug:slug>/", views.category_posts, name="category_posts"),
    path("tag/<slug:slug>/", views.tagged_posts, name="tagged_posts"),
    path("delete-account/", views.delete_account, name="delete_account"),
    path(
        "account-deleted/",
        TemplateView.as_view(template_name="blog/account_deleted.html"),
        name="account_deleted",
    ),
]
