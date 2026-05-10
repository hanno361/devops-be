import pytest
from rest_framework.test import APIClient
from apps.blog.models import BlogCategory, BlogPost, BlogTag

@pytest.fixture
def tech_blog_data(db):
    cat = BlogCategory.objects.create(name="Yazılım Mimarisi")
    tag = BlogTag.objects.create(name="Clean Code")
    
    # 1 Yayınlanmış yazı
    post_pub = BlogPost.objects.create(
        category=cat, 
        title="Microservis Mimarisine Geçiş", 
        body="Detaylar...",
        status="published"
    )
    post_pub.tags.add(tag)
    
    # 1 Taslak yazı (API'den dönmemesi lazım)
    BlogPost.objects.create(
        category=cat, 
        title="Henüz Bitmemiş Yazı", 
        body="...",
        status="draft"
    )
    return post_pub

@pytest.mark.django_db
class TestBlogAPI:
    def test_blog_list_returns_only_published(self, api_client, tech_blog_data):
        # Listeleme endpointi - slash yok
        response = api_client.get("/api/blog")
        
        assert response.status_code == 200
        data = response.json()
        
        # List endpoints "data" ve "meta" zarfında (envelope) dönüyor (README'ye göre)
        assert "data" in data
        assert len(data["data"]) == 1
        assert data["data"][0]["title"] == "Microservis Mimarisine Geçiş"

    def test_blog_detail_returns_published(self, api_client, tech_blog_data):
        # Detay endpointi - slash yok
        slug = tech_blog_data.slug
        response = api_client.get(f"/api/blog/{slug}")
        
        assert response.status_code == 200
        data = response.json()["data"]
        
        assert data["title"] == "Microservis Mimarisine Geçiş"
        assert data["slug"] == slug

    def test_blog_detail_returns_404_for_draft(self, api_client, tech_blog_data):
        # Taslak yazının slug'ını isteyelim
        cat = BlogCategory.objects.first()
        draft = BlogPost.objects.create(category=cat, title="Gizli", status="draft")
        
        response = api_client.get(f"/api/blog/{draft.slug}")
        
        # Taslak yazılar API'den dönmediği için 404 Not Found vermelidir
        assert response.status_code == 404