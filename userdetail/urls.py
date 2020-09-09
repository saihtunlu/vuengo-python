from django.urls import path
from .views import UploadDetail, ChangeAvatar, GetAuth, GetUser, ChangePasswordView

urlpatterns = [
    path('upload-detail/', UploadDetail.as_view()),
    path('change-avatar/', ChangeAvatar.as_view()),
    path('auth/', GetAuth.as_view()),
    path('contents/', GetUser.as_view()),
    path('update-password/', ChangePasswordView.as_view()),
]
