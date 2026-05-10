import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from apps.catalog.models import Category, Product
from apps.wishlist.models import WishlistItem

User = get_user_model()

@pytest.fixture
def user1(db):
    return User.objects.create_user(username="user1", email="user1@test.com", password="pwd")

@pytest.fixture
def user2(db):
    return User.objects.create_user(username="user2", email="user2@test.com", password="pwd")

@pytest.fixture
def product(db):
    cat = Category.objects.create(name="Akıllı Telefonlar")
    return Product.objects.create(category=cat, name="Samsung Galaxy S24", price=45000.0)

@pytest.mark.django_db
class TestWishlistAPI:
    def test_unauthenticated_access_denied(self, api_client):
        # Giriş yapmadan listeye erişim 401 dönmeli (Slash olmadan)
        response = api_client.get("/api/wishlist/") 
        assert response.status_code == 401

    def test_user_can_only_see_own_wishlist(self, user1, user2, product):
        WishlistItem.objects.create(user=user1, product=product)
        WishlistItem.objects.create(user=user2, product=product)

        client = APIClient()
        client.force_authenticate(user=user1)
        
        response = client.get("/api/wishlist/")
        assert response.status_code == 200
        
        # User1'in isteğinde sadece kendi eklediği 1 adet ürün dönmeli
        data = response.json()
        assert len(data) == 1

    def test_create_wishlist_item(self, user1, product):
        client = APIClient()
        client.force_authenticate(user=user1)
        
        payload = {"product_id": product.id}
        response = client.post("/api/wishlist/", payload, format="json")
        
        assert response.status_code == 201
        assert WishlistItem.objects.filter(user=user1, product=product).exists()

    def test_delete_wishlist_item(self, user1, product):
        item = WishlistItem.objects.create(user=user1, product=product)
        
        client = APIClient()
        client.force_authenticate(user=user1)
        
        # Silme işlemi (URL'in sonuna slash koymuyoruz)
        response = client.delete(f"/api/wishlist/{item.id}/")
        assert response.status_code == 204
        assert not WishlistItem.objects.filter(id=item.id).exists()