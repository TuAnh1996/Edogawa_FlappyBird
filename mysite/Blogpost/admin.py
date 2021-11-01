from django.contrib import admin
from .models import Post, Comment
# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']#lọc bài theo date
    search_fields = ['title']
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)