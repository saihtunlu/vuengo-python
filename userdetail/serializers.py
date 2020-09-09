from rest_framework import serializers
from .models import Detail
from django.contrib.auth.models import User


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    detail = DetailSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email',  'detail']


class ChangeAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ['avatar']


class UserSerializer(serializers.ModelSerializer):

    detail = DetailSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email',  'detail']


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ChangePersonalSerializer(serializers.Serializer):
    model = User
    """
    Serializer for password change endpoint.
    """
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
