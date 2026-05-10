import pytest
from rest_framework.test import APIClient

from apps.home.models import Banner, BannerFeature, FeaturedProduct, HeroSlide
# Diğer app'lerden (catalog ve blog) importlar
from apps.catalog.models import Category, Product
# BlogCategory'yi de import ediyoruz
from apps.blog.models import BlogCategory, BlogPost


@pytest.mark.django_db
class TestHomeAPI:
    def test_hero_slides_returns_active_only(self, api_client):
        HeroSlide.objects.create(title="Aktif Slide (Monitör)", bg="/bg1.jpg", is_active=True)
        HeroSlide.objects.create(title="Pasif Slide (Eski Kasa)", bg="/bg2.jpg", is_active=False)

        response = api_client.get("/api/home/hero-slides")
        
        assert response.status_code == 200
        data = response.json()["data"]
        assert len(data) == 1
        assert data[0]["title"] == "Aktif Slide (Monitör)"

    def test_featured_products_returns_active_only(self, api_client):
        FeaturedProduct.objects.create(title="Öne Çıkan Klavye", image_src="/klavye.jpg", is_active=True)
        FeaturedProduct.objects.create(title="Tükenen Kulaklık", image_src="/kulaklik.jpg", is_active=False)

        response = api_client.get("/api/home/featured-products")
        
        assert response.status_code == 200
        data = response.json()["data"]
        assert len(data) == 1
        assert data[0]["title"] == "Öne Çıkan Klavye"

    def test_banner_returns_404_if_unconfigured(self, api_client):
        response = api_client.get("/api/home/banner")
        assert response.status_code == 404

    def test_banner_returns_200_with_features(self, api_client):
        banner = Banner.objects.create(title="Yazılım Geliştirici Kampanyası", background_image="/banner.jpg")
        BannerFeature.objects.create(banner=banner, icon="code", label="Ücretsiz Lisans")

        response = api_client.get("/api/home/banner")
        
        assert response.status_code == 200
        data = response.json()["data"]
        assert data["title"] == "Yazılım Geliştirici Kampanyası"
        assert len(data["features"]) == 1
        assert data["features"][0]["label"] == "Ücretsiz Lisans"

    def test_home_products_returns_featured_active_products(self, api_client):
        cat = Category.objects.create(name="Sunucu Çözümleri")
        
        # Benzersiz 'sku' değerlerini ekledik
        Product.objects.create(
            category=cat, name="Rack Tipi Sunucu", sku="SRV-001", 
            price=50000.0, is_active=True, is_featured=True
        )
        Product.objects.create(
            category=cat, name="Tower Sunucu", sku="SRV-002", 
            price=30000.0, is_active=True, is_featured=False
        )

        response = api_client.get("/api/home/products")
        assert response.status_code == 200
        data = response.json()["data"]
        assert len(data) == 1
        assert data[0]["name"] == "Rack Tipi Sunucu"

    def test_home_blog_returns_published_only(self, api_client):
        # BlogPost oluşturabilmek için zorunlu olan BlogCategory'yi oluşturduk
        blog_cat = BlogCategory.objects.create(name="Teknoloji", slug="teknoloji")

        # Yazılara 'category' atamasını yaptık
        BlogPost.objects.create(
            category=blog_cat, title="React vs Compose", 
            slug="react-vs-compose", status="published"
        )
        BlogPost.objects.create(
            category=blog_cat, title="Taslak Yazı", 
            slug="taslak-yazi", status="draft"
        )

        response = api_client.get("/api/home/blog")
        assert response.status_code == 200
        data = response.json()["data"]
        assert len(data) == 1
        assert data[0]["title"] == "React vs Compose"