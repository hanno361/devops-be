from decimal import Decimal

import pytest
from django.urls import reverse

from apps.catalog.models import Category, Product


@pytest.fixture
def product(db):
    cat = Category.objects.create(name="EDP")
    return Product.objects.create(
        category=cat, name="Item", sku="SKU-1", price=Decimal("50"), stock=5
    )


@pytest.mark.django_db
def test_my_cart_requires_auth(api_client):
    response = api_client.get(reverse("my-cart"))
    assert response.status_code == 401


@pytest.mark.django_db
def test_add_item_creates_cart_and_item(auth_client, product):
    response = auth_client.post(
        reverse("cart-item-add"),
        {"product_id": product.id, "quantity": 2},
        format="json",
    )
    assert response.status_code == 201
    cart = auth_client.get(reverse("my-cart")).json()
    assert cart["item_count"] == 2
    assert Decimal(cart["total"]) == Decimal("100.00")


@pytest.mark.django_db
def test_add_same_product_increments_quantity(auth_client, product):
    auth_client.post(
        reverse("cart-item-add"),
        {"product_id": product.id, "quantity": 1},
        format="json",
    )
    auth_client.post(
        reverse("cart-item-add"),
        {"product_id": product.id, "quantity": 2},
        format="json",
    )
    cart = auth_client.get(reverse("my-cart")).json()
    assert cart["item_count"] == 3
