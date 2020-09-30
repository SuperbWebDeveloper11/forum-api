from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import PostSerializer# , CommentSerializer
from .models import Post, Comment
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # associating each post with a user (In post creation)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
                           

'''
class CommentList(APIView):
    def get(self, request, pk):
        queryset = Comment.objects.filter(post__pk=pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        comment_body = request.data.get("body")
        comment_owner = request.user
        comment_post = get_object_or_404(Post, pk=pk)
        new_comment = {
                'body': comment_body,
                'owner': comment_owner,
                'post': comment_post,
                }
        serializer = CommentSerializer(data=new_comment)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
                       
 
class CommentDetail(APIView):
    def get(self, request, pk, comment_pk):
        queryset = get_object_or_404(Comment, comment_pk)
        serializer = CommentSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, comment_pk):
        queryset = get_object_or_404(Comment, comment_pk)
        new_comment = {'body': request.data.get('body')}
        serializer = CommentSerializer(instance=queryset, data=new_comment)
        return Response(serializer.data)
                       
    def delete(self, request, pk, comment_pk):
        queryset = get_object_or_404(Comment, comment_pk)
        queryset.delete()
        return Response({})

'''
