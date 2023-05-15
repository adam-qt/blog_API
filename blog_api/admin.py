from django.contrib import admin
from .models import Post, Comment

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','text','created', 'owner', ]
    search_fields = ['title','created']
    ordering = ['title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
# Register your models here.
