from .models import Post, Like, Comment, CommentReplies, CommentLike
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .serializers import PostSerializers, LikeSerializers, CommentSerializers, CommentRepliesSerializers, CommentLikeSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

# Create your views here.


class PostsView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.order_by('created_at').reverse()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializers(queryset, many=True)
        return Response(serializer.data)


class CreatePost(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data
        post = Post(user=self.request.user)
        post_serializer = PostSerializers(post, data=data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthPost(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        queryset = Post.objects.filter(user=user_id)
        serializer = PostSerializers(queryset, many=True)
        return Response(serializer.data)


class RemovePost(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        Post.objects.get(user=self.request.user,
                         id=request.data['post_id']).delete()
        return Response('Success', status=status.HTTP_201_CREATED)


# Like
class AddLike(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data
        LikedPost = Post.objects.get(id=request.data['post_id'])
        like = Like(user=self.request.user,
                    post=LikedPost)  # add foreign key
        like_serializer = LikeSerializers(like, data=data)
        if like_serializer.is_valid():
            like_serializer.save()
            return Response('Success', status=status.HTTP_201_CREATED)
        else:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)


class RemoveLike(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        Like.objects.get(user=self.request.user,
                         post=request.data['post_id']).delete()
        return Response('Success', status=status.HTTP_201_CREATED)

# Comments


class AddComment(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data
        LikedPost = Post.objects.get(id=request.data['post_id'])
        comment = Comment(user=self.request.user,
                          post=LikedPost)  # add foreign key
        comment_serializer = CommentSerializers(comment, data=data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveComment(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        Comment.objects.get(user=self.request.user,
                            id=request.data['comment_id']).delete()
        return Response('Success', status=status.HTTP_201_CREATED)

# Comment-replies


class AddCommentReply(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data
        RepliedComment = Comment.objects.get(id=request.data['comment_id'])
        commentReply = CommentReplies(user=self.request.user,
                                      comment=RepliedComment)  # add foreign key
        comment_reply_serializer = CommentRepliesSerializers(
            commentReply, data=data)
        if comment_reply_serializer.is_valid():
            comment_reply_serializer.save()
            return Response(comment_reply_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comment_reply_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveCommentReply(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        CommentReplies.objects.get(user=self.request.user,
                                   id=request.data['reply_id']).delete()
        return Response('Success', status=status.HTTP_201_CREATED)

# comment-likes


class AddCommentLike(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data
        LikedComment = get_object_or_404(
            Comment, id=request.data['comment_id'])
        like = CommentLike(user=self.request.user,
                           comment=LikedComment)  # add foreign key
        like_serializer = CommentLikeSerializers(like, data=data)
        if like_serializer.is_valid():
            like_serializer.save()
            return Response(like_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(like_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveCommentLike(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        CommentLike.objects.get(user=self.request.user,
                                comment=request.data['comment_id']).delete()
        return Response('Success', status=status.HTTP_201_CREATED)
