from django.contrib import admin
from .models import Post, CommentLike, Comment, CommentReplies, Like
# Register your models here.
Models = [Post, CommentLike, Comment, CommentReplies, Like]
admin.site.register(Models)
