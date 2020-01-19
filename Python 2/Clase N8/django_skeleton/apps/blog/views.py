from rest_framework import viewsets
from .models import Comments, Post
from .serialize import CommertsSerializer, PostSerializer


class CommentsViewset(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommertsSerializer


class PostSerializer(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
