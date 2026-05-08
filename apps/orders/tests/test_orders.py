from decimal import Decimal

import pytest
from django.urls import reverse

from apps.cart.models import Cart, CartItem
from apps.catalog.models import Category, Product
from apps.orders.models import Order


@pytest.fixture
def product(db):
    cat = Category.objects.create(name="EDP")
    return Product.objects.create(
        category=cat, name="P", sku="P-1", price=Decimal("100"), stock=5
    )


@pytest.fixture
def address():
    return {
        "full_name": "Test User",
        "email": "test@test.local",
        "address_line1": "1 Test Lane",
        "city": "Istanbul",
        "country": "Türkiye",
    }


@pytest.mark.django_db
def test_checkout_requires_auth(api_client, address):
    response = api_client.post(reverse("checkout"), address, format="json")
    assert response.status_code == 401


@pytest.mark.django_db
def test_checkout_fails_when_cart_empty(auth_client, address):
    response = auth_client.post(reverse("checkout"), address, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_checkout_creates_order_and_clears_cart(auth_client, user, product, address):
    cart = Cart.objects.create(user=user)
    CartItem.objects.create(cart=cart, product=product, quantity=2)

    response = auth_client.post(reverse("checkout"), address, format="json")
    assert response.status_code == 201
    body = response.json()
    assert body["status"] == "pending"
    assert Decimal(body["subtotal"]) == Decimal("200.00")
    assert len(body["items"]) == 1

    product.refresh_from_db()
    assert product.stock == 3
    assert cart.items.count() == 0


@pytest.mark.django_db
def test_my_orders_only_lists_own(auth_client, user, product, address):
    cart = Cart.objects.create(user=user)
    CartItem.objects.create(cart=cart, product=product, quantity=1)
    auth_client.post(reverse("checkout"), address, format="json")

    response = auth_client.get(reverse("my-orders"))
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 1
    assert Order.objects.filter(user=user).count() == 1
