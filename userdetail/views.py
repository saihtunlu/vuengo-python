from .models import Detail
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from .serializers import DetailSerializer, ChangeAvatarSerializer, UserSerializer, ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.db.models import Q
# Create your views here.


class UploadDetail(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id
        detail_serializer = DetailSerializer(data=data)
        if detail_serializer.is_valid():
            detail_serializer.save()
            return Response(detail_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangeAvatar(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        detail = Detail.objects.filter(
            user=user, id=request.data['id']).first()
        changeAvatarSerializer = ChangeAvatarSerializer(detail, data=data)
        if changeAvatarSerializer.is_valid():
            changeAvatarSerializer.save()
            return Response(changeAvatarSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(changeAvatarSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAuth(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        id = request.user.id
        queryset = User.objects.get(id=id)
        serializer = UserSerializer(queryset, many=False)
        return Response(serializer.data)


class GetUser(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        id = request.user.id
        queryset = User.objects.filter(~Q(id=id))
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class ChangePasswordView(APIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         refresh = self.get_token(self.user)
#         data['refresh'] = str(refresh)
#         data['access'] = str(refresh.access_token)

#         # Add extra responses here
#         data['username'] = self.user.username
#         data['id'] = self.user.id
#         data['groups'] = self.user.groups.values_list('name', flat=True)
#         return data


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
