from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import PostSerializer
from .models import Post
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # associating each post with a user (In post creation)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['get'])
    def comments(self, request, *args, **kwargs):
        # post = self.get_object()
        post_comments = []
        return Response(post_comments)
                            

'''
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # associating each post with a user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
'''
                        

