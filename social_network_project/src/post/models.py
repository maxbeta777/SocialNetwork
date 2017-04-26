from django.db import models

from user.models import User
from recipe.models import Recipe


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    user = models.ForeignKey(User, blank=True, null=True, default=None)
    recipe = models.ForeignKey(Recipe, blank=True, null=True, default=None)
    estimation = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Пост %s" % self.id


class PostImage(models.Model):

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    post = models.ForeignKey(Post, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='post_images/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return " %s" % self.id


class Comment(models.Model):
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    post = models.ForeignKey(Post, blank=True, null=True, default=None)
    user = models.ForeignKey(User, blank=True, null=True, default=None)
    comment_text = models.TextField(blank=True, null=True, default=None)
    estimation = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s" % self.id


class PostType(models.Model):
    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types of Post'

    post = models.ForeignKey(Post, blank=True, null=True, default=None)
    type = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.type