
from django.contrib import admin
from .models import Post, Comment

class AdminComment(admin.StackedInline):
    model = Comment
    extra = 1

class AdminPost(admin.ModelAdmin):
    inlines = [AdminComment]


admin.site.register(Post, AdminPost)
#admin.site.register(Comment)
