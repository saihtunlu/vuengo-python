from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('', include('userdetail.urls')),
    path('', include('chat.urls')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('rest_registration.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
