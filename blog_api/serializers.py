from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username','posts','comments']




class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model= models.Comment
        fields=['id','created','text','owner','post']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many = True)
    class Meta:
        model = models.Post
        fields = ['id','title','created','owner','text','comments']