from django.contrib import admin
from unicodedata import category

from .models import Category, Tag, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','category','author', 'description', 'created_at', 'is_published']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published', 'category']
    list_filter = ['is_published', 'category', 'created_at', 'tags']
    search_fields = ['title', 'description']
    filter_horizontal = ['tags']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'author','created_at', 'is_active']
    list_editable = ['is_active']
    list_filter = ['is_active', 'created_at', 'post']
    search_fields = ['content','author']

