from django.contrib import admin
from .models import Post, Category, Comment, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published', 'created')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('published', 'created', 'category', 'tags')
    search_fields = ('title', 'body')
    filter_horizontal = ('tags',)  # Enables tag selection in admin

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
