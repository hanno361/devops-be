import pytest
from decimal import Decimal
from rest_framework.test import APIClient
from apps.catalog.models import Category, Product

@pytest.fixture
def active_product(db):
    cat = Category.objects.create(name="Bulut Cozumleri")
    return Product.objects.create(
        category=cat, name="AWS Kredisi", sku="AWS-100", 
        price=Decimal("100.00"), is_active=True
    )

@pytest.fixture
def inactive_product(db):
    cat = Category.objects.create(name="Eski Donanimlar")
    return Product.objects.create(
        category=cat, name="Eski Sunucu", sku="OLD-1", 
        price=Decimal("50.00"), is_active=False
    )

@pytest.mark.django_db
class TestCatalogAPI:
    def test_product_list_returns_only_active(self, api_client, active_product, inactive_product):
        # README kuralı: slash yok
        response = api_client.get("/api/products")
        
        assert response.status_code == 200
        data = response.json()["data"]
        
        assert len(data) == 1
        assert data[0]["name"] == "AWS Kredisi"
        # Listelemede inactive_product gelmemeli

    def test_product_detail_returns_active(self, api_client, active_product):
        response = api_client.get(f"/api/products/{active_product.slug}")
        
        assert response.status_code == 200
        assert response.json()["data"]["name"] == "AWS Kredisi"

    def test_product_detail_returns_404_for_inactive(self, api_client, inactive_product):
        response = api_client.get(f"/api/products/{inactive_product.slug}")
        
        # Pasif ürünün detay sayfası da bulunamamalı
        assert response.status_code == 404