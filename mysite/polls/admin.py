from django.contrib import admin
from .models import Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['body','date']#hien thi ra
    list_filter = ['date']#lọc bài theo date
    search_fields = ['date']
    # inlines = [CommentInline]

admin.site.register(Comment, PostAdmin)
# admin.site.register(Comment)