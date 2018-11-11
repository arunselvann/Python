from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from posts.models import post
from.serializers import PostListSerializer, PostDetailSerializer, PostCreateSerializer
from .permissions import IsOwnerOrReadOnly


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostListAPIView(ListAPIView):
    queryset = post.objects.all()
    serializer_class = PostListSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = post.objects.all()
    serializer_class = PostListSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PostDestroyAPIView(DestroyAPIView):
    queryset = post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'