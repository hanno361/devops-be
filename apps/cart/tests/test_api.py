import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from apps.catalog.models import Category, Product
from apps.cart.models import Cart, CartItem

User = get_user_model()

@pytest.fixture
def auth_client_and_user(db):
    user = User.objects.create_user(email="user@cart.local", username="user", password="pwd")
    client = APIClient()
    client.force_authenticate(user=user)
    return client, user

@pytest.fixture
def product(db):
    cat = Category.objects.create(name="Akıllı Telefonlar")
    return Product.objects.create(category=cat, name="Android Test Cihazı", price=20000.0,sku="PHN-001")

@pytest.mark.django_db
class TestCartAPI:
    def test_get_cart_auto_creates_if_not_exists(self, auth_client_and_user):
        client, user = auth_client_and_user
        
        # Henüz veritabanında sepet yok
        assert Cart.objects.filter(user=user).exists() is False
        
        response = client.get(reverse("my-cart"))
        assert response.status_code == 200
        
        # _get_or_create_cart çalıştığı için sepet oluşmuş olmalı
        assert Cart.objects.filter(user=user).exists() is True
        assert response.json()["item_count"] == 0

    def test_add_item_to_cart(self, auth_client_and_user, product):
        client, user = auth_client_and_user
        
        payload = {"product_id": product.id, "quantity": 2}
        response = client.post(reverse("cart-item-add"), payload, format="json")
        
        assert response.status_code == 201
        assert response.json()["quantity"] == 2

    def test_add_existing_item_increments_quantity(self, auth_client_and_user, product):
        client, user = auth_client_and_user
        
        # Aynı ürünü iki farklı istekte ekliyoruz
        client.post(reverse("cart-item-add"), {"product_id": product.id, "quantity": 1}, format="json")
        response = client.post(reverse("cart-item-add"), {"product_id": product.id, "quantity": 3}, format="json")
        
        # Yeni bir kayıt açmak yerine üzerine 1+3=4 olarak eklemeli
        assert response.status_code == 200 # created değil, ok döndüğünü doğrular
        assert CartItem.objects.count() == 1
        assert CartItem.objects.first().quantity == 4

    def test_update_item_quantity(self, auth_client_and_user, product):
        client, user = auth_client_and_user
        cart = Cart.objects.create(user=user)
        item = CartItem.objects.create(cart=cart, product=product, quantity=1)
        
        # Miktarı 5 olarak güncelliyoruz (PATCH)
        response = client.patch(
            reverse("cart-item-detail", args=[item.id]), 
            {"quantity": 5}, 
            format="json"
        )
        assert response.status_code == 200
        
        item.refresh_from_db()
        assert item.quantity == 5

    def test_delete_cart_item(self, auth_client_and_user, product):
        client, user = auth_client_and_user
        cart = Cart.objects.create(user=user)
        item = CartItem.objects.create(cart=cart, product=product, quantity=1)
        
        response = client.delete(reverse("cart-item-detail", args=[item.id]))
        assert response.status_code == 204
        assert CartItem.objects.count() == 0

    def test_clear_cart(self, auth_client_and_user, product):
        client, user = auth_client_and_user
        cart = Cart.objects.create(user=user)
        CartItem.objects.create(cart=cart, product=product, quantity=2)
        
        response = client.post(reverse("cart-clear"))
        assert response.status_code == 204
        
        # Sepetin kendisi duruyor ama içindeki öğeler silinmiş olmalı
        assert Cart.objects.count() == 1
        assert CartItem.objects.count() == 0