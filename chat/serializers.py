from rest_framework import serializers
from .models import ChatSession, ChatSessionMessage
from userdetail.serializers import OwnerSerializer


class ChatSessionSerializers(serializers.ModelSerializer):
    creator = OwnerSerializer(many=False, read_only=True)
    invited_user = OwnerSerializer(many=False, read_only=True)
    # post = PostSerializers(many=False, read_only=True)

    class Meta:
        model = ChatSession
        fields = ['id', 'uri',  'creator', 'invited_user']


class ChatMessageSerializers(serializers.ModelSerializer):
    user = OwnerSerializer(many=False, read_only=True)
    chat_session = ChatSessionSerializers(many=False, read_only=True)

    class Meta:
        model = ChatSessionMessage
        fields = ['id', 'user',  'text', 'chat_session',
                  'create_date', 'update_date', 'image', 'received', 'seen']
