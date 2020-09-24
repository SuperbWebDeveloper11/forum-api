from django.contrib.auth.models import User, Group
from rest_framework import serializers
from articles.models import Article
from posts.models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # list of primary keys of articles created by the user Ex : [2, 5]
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'articles', 'posts']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


