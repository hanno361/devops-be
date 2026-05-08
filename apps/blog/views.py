from rest_framework import generics, permissions

from .models import BlogCategory, BlogPost, BlogTag
from .serializers import (
    BlogCategorySerializer,
    BlogPostDetailSerializer,
    BlogPostListSerializer,
    BlogTagSerializer,
)


class BlogCategoryListView(generics.ListAPIView):
    serializer_class = BlogCategorySerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None
    queryset = BlogCategory.objects.all()


class BlogTagListView(generics.ListAPIView):
    serializer_class = BlogTagSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None
    queryset = BlogTag.objects.all()


class BlogPostListView(generics.ListAPIView):
    serializer_class = BlogPostListSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = {
        "category__slug": ["exact"],
        "tags__slug": ["exact"],
    }
    search_fields = ("title", "excerpt", "body")
    ordering_fields = ("published_at", "created_at", "title")

    def get_queryset(self):
        return (
            BlogPost.objects.filter(status=BlogPost.PUBLISHED)
            .select_related("category", "author")
            .prefetch_related("tags")
        )


class BlogPostDetailView(generics.RetrieveAPIView):
    serializer_class = BlogPostDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"

    def get_queryset(self):
        return (
            BlogPost.objects.filter(status=BlogPost.PUBLISHED)
            .select_related("category", "author")
            .prefetch_related("tags")
        )
