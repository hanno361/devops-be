import pytest
from datetime import datetime, timezone
from apps.blog.models import BlogCategory, BlogPost
from apps.blog.serializers import BlogPostSerializer

@pytest.mark.django_db
class TestBlogPostSerializer:
    def test_get_date_uses_published_at_if_available(self):
        cat = BlogCategory.objects.create(name="Tech")
        dt = datetime(2026, 5, 10, tzinfo=timezone.utc)
        
        post = BlogPost.objects.create(category=cat, title="Haber", body="İçerik", published_at=dt)
        serializer = BlogPostSerializer(post)
        
        # strftime("%d %B, %Y") -> "10 May, 2026" olmalı (yerel ayara göre "May" değişebilir)
        # Sadece gün ve yıl kısmının tuttuğunu doğrulamak daha güvenli
        assert "10" in serializer.data["date"]
        assert "2026" in serializer.data["date"]

    def test_get_image_priority(self):
        cat = BlogCategory.objects.create(name="DevOps")
        
        # Sadece cover_url var
        post1 = BlogPost.objects.create(category=cat, title="P1", body="B", cover_url="https://img.com/p1.jpg")
        serializer1 = BlogPostSerializer(post1)
        assert serializer1.data["image"] == "https://img.com/p1.jpg"

        # İkisi de yok
        post2 = BlogPost.objects.create(category=cat, title="P2", body="B")
        serializer2 = BlogPostSerializer(post2)
        assert serializer2.data["image"] == ""