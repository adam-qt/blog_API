from django.contrib import admin
from .models import Post, Comment, Categories

# admin.site.register(Post)


class CommentInline(admin.TabularInline):
    model = Comment


class CategoryInLine(admin.TabularInline):
    model = Categories


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['title', 'text', 'created', 'owner', ]
    search_fields = ['title', 'created']
    ordering = ['title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ['text', 'owner']
