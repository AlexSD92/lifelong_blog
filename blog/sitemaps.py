from .models import Post, Tag, Category
from django.urls import reverse
from django.contrib.sitemaps import Sitemap


# Post sitemap (already working)
class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.filter(published=True).order_by('-created')

    def lastmod(self, obj):
        return obj.created

# Tag sitemap
class TagSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Tag.objects.all()

    def location(self, obj):
        return reverse('tagged_posts', args=[obj.slug])

# Category sitemap
class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return reverse('category_posts', args=[obj.slug])
    
# Static pages
class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['privacy', 'terms', 'delete_account']

    def location(self, item):
        return reverse(item)

