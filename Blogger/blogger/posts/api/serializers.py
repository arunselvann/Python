from rest_framework.serializers import ModelSerializer
from posts.models import post


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = post
        fields = [
            'title',
            'content',
            'publish',
            'image'
        ]


class PostListSerializer(ModelSerializer):
    class Meta:
        model = post
        fields = [
            'user',
            'title',
            'slug',
            'content',
            'publish',
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish',
        ]