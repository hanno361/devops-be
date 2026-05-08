from rest_framework import serializers

from .models import BlogCategory, BlogPost, BlogTag


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ("id", "name", "slug")


class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = ("id", "name", "slug")


class BlogPostListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="slug", read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    cover_url = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = (
            "id",
            "title",
            "slug",
            "excerpt",
            "category",
            "author",
            "cover_url",
            "published_at",
        )

    def get_cover_url(self, obj):
        if not obj.cover:
            return None
        request = self.context.get("request")
        return request.build_absolute_uri(obj.cover.url) if request else obj.cover.url


class BlogPostDetailSerializer(BlogPostListSerializer):
    category = BlogCategorySerializer(read_only=True)
    tags = BlogTagSerializer(many=True, read_only=True)

    class Meta(BlogPostListSerializer.Meta):
        fields = BlogPostListSerializer.Meta.fields + ("body", "tags")
