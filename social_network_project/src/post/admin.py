from django.contrib import admin
from .models import *


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]
    inlines = [PostImageInline]

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)


class PostImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PostImage._meta.fields]

    class Meta:
        model = PostImage

admin.site.register(PostImage, PostImageAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]

    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)

