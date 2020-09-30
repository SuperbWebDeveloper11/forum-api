from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post, Comment


'''
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['body'] 
'''


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    refined_body= serializers.CharField(read_only=True)
    # comments = CommentSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'refined_body', 'owner', 'comments'] 

