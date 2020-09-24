from rest_framework import serializers
from .models import Article
from posts.models import Post


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    refined_body= serializers.CharField(read_only=True)
    class Meta:
        model = Article
        fields = ['id', 'title', 'body', 'refined_body', 'owner'] 



