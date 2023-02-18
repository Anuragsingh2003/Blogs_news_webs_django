from django.contrib import admin

from .models import Blog,NewsArticle
# Register your models here.


class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','published_at')

admin.site.register(Blog,BlogAdmin)
admin.site.register(NewsArticle,NewsArticleAdmin)