from numpy import generic
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from . import serializers
from .models import Profile, Post, Comment

class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_class = (AllowAny,)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.object.all()
    serializer_class = serializers.ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(userProfile=self.request.user)


class MyProfileListView(generic.ListAPIlView):
    queryset = Profile.object.all()
    serializer_class = serializers.ProfileSerializer

    def get_queryset(self):
        return self.queryset.filter(userProfile=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.object.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(userPost=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.object.all()
    serializer_class = serializers.CommentSerializer

    def perform_create(self, serializer):
        serializer.save(userComment=self.request.user)

