from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'text', 'image', 'description', 'created_at')


class UploadSerializer(serializers.Serializer):
    image = serializers.ImageField()
