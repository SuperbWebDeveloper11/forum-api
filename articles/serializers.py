from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    refined_body= serializers.CharField(read_only=True)
    class Meta:
        model = Article
        fields = ['id', 'title', 'body', 'refined_body', 'owner'] 


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # list of primary keys of articles created by the user Ex : [2, 5]
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'articles']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


