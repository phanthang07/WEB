from django.contrib import admin
from .models import Post,Comment
# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comment

class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date']
    list_filter = ['date']
    search_fields = ['title']
    inlines = [CommentInLine]
admin.site.register(Post, PostsAdmin)
