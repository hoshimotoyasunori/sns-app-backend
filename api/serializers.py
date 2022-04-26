from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile, Post, Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwards = {'password': {'write_only': True}}

    def create(self, validated_data):

        user = get_user_model().objects.object.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    credated_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'nickName', 'userProfile', 'created_at', 'img')
        extra_kwards = {'userProfile': {'read_only': True}}


class PostSerializer(serializers.ModelSerializer):
    credated_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'userPost', 'created_at', 'img', 'liked')
        extra_kwards = {'userPost': {'read_only': True}}


class CommentSerializer(serializers.ModelSerializer):
    credated_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'userComment', 'post')
        extra_kwards = {'userComment': {'read_only': True}}
