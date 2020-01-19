from rest_framework import serializers
from .models import Comments, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CommertsSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.filter())

    class Meta:
        model = Comments
        fields = ('name', 'email', 'website', 'post', 'message',)


