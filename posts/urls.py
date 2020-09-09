from django.urls import path
from .views import PostsView, CreatePost, AuthPost, RemovePost, AddComment, RemoveComment, AddLike, RemoveLike, AddCommentReply, RemoveCommentReply, AddCommentLike, RemoveCommentLike

urlpatterns = [
    path('posts/', PostsView.as_view(), name='posts_view'),
    path('create-post/', CreatePost.as_view(), name='create_post'),
    path('delete-post/', RemovePost.as_view(), name='remove_post'),
    path('my-posts/', AuthPost.as_view(), name='my_posts'),
    path('comment/', AddComment.as_view()),
    path('remove-comment/', RemoveComment.as_view()),
    path('like/', AddLike.as_view()),
    path('unlike/', RemoveLike.as_view()),
    path('comment-reply/', AddCommentReply.as_view()),
    path('remove-comment-reply/', RemoveCommentReply.as_view()),
    path('like-comment/', AddCommentLike.as_view()),
    path('unlike-comment/', RemoveCommentLike.as_view()),
]
