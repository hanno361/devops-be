from rest_framework import generics, permissions

from apps.core.mixins import EnvelopeRetrieveMixin

from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]
    search_fields = ("title", "excerpt", "body")
    ordering_fields = ("published_at", "created_at", "title")
    ordering = ("-published_at",)

    def get_queryset(self):
        return (
            BlogPost.objects.filter(status=BlogPost.PUBLISHED)
            .select_related("category", "author")
            .prefetch_related("tags")
        )


class BlogPostDetailView(EnvelopeRetrieveMixin, generics.RetrieveAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"

    def get_queryset(self):
        return BlogPost.objects.filter(status=BlogPost.PUBLISHED)
