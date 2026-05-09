from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    content = serializers.CharField(source="body", read_only=True)

    class Meta:
        model = BlogPost
        fields = (
            "id",
            "slug",
            "title",
            "date",
            "comments",
            "excerpt",
            "image",
            "content",
        )

    def get_id(self, obj) -> str:
        return str(obj.id)

    def get_date(self, obj) -> str:
        target = obj.published_at or obj.created_at
        return target.strftime("%d %B, %Y")

    def get_comments(self, obj) -> int:
        return 0

    def get_image(self, obj) -> str:
        if not obj.cover:
            return ""
        request = self.context.get("request")
        url = obj.cover.url
        return request.build_absolute_uri(url) if request else url
