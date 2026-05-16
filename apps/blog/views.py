from collections import OrderedDict

from django.db.models.functions import TruncMonth
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.mixins import EnvelopeRetrieveMixin

from .models import BlogPost, BlogTag
from .serializers import BlogPostSerializer


class BlogPostListView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]
    search_fields = ("title", "excerpt", "body")
    ordering_fields = ("published_at", "created_at", "title")
    ordering = ("-published_at",)

    def get_queryset(self):
        qs = (
            BlogPost.objects.filter(status=BlogPost.PUBLISHED)
            .select_related("category", "author")
            .prefetch_related("tags")
        )
        params = self.request.query_params

        tag = params.get("tag")
        if tag:
            qs = qs.filter(tags__slug=tag)

        year = params.get("year")
        if year:
            qs = qs.filter(published_at__year=year)

        month = params.get("month")
        if month:
            qs = qs.filter(published_at__month=month)

        return qs.distinct()


class BlogPostDetailView(EnvelopeRetrieveMixin, generics.RetrieveAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"

    def get_queryset(self):
        return BlogPost.objects.filter(status=BlogPost.PUBLISHED)


class BlogTagListView(generics.ListAPIView):
    """Flat list of all blog tags (sidebar)."""

    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def get_queryset(self):
        return BlogTag.objects.order_by("name")

    def list(self, request, *args, **kwargs):
        tags = [
            {"name": tag.name, "slug": tag.slug} for tag in self.get_queryset()
        ]
        return Response(tags)


class BlogArchiveView(APIView):
    """Year/Month-grouped archive for the blog sidebar.

    Returns:
        [
          {"month": "April 2021",
           "year": 2021, "monthNumber": 4,
           "posts": [{"title": "...", "slug": "..."}, ...]},
          ...
        ]
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        qs = (
            BlogPost.objects.filter(status=BlogPost.PUBLISHED, published_at__isnull=False)
            .order_by("-published_at")
        )

        archive = OrderedDict()
        for post in qs:
            key = (post.published_at.year, post.published_at.month)
            entry = archive.setdefault(
                key,
                {
                    "month": post.published_at.strftime("%B %Y"),
                    "year": key[0],
                    "monthNumber": key[1],
                    "posts": [],
                },
            )
            entry["posts"].append({"title": post.title, "slug": post.slug})

        return Response(list(archive.values()))
