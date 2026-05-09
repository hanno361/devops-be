from decimal import Decimal

import pytest
from django.urls import reverse

from apps.catalog.models import Category, Product
from apps.orders.models import Order


@pytest.fixture
def product(db):
    cat = Category.objects.create(name="EDP")
    return Product.objects.create(
        category=cat, name="Velvet", sku="V-1", price=Decimal("100"), stock=5
    )


def _payload(product, quantity=2):
    return {
        "items": [
            {
                "productId": str(product.id),
                "productName": product.name,
                "quantity": quantity,
                "price": float(product.effective_price),
            }
        ],
        "shipping": {
            "name": "Test User",
            "email": "test@test.local",
            "phone": "0000",
            "address": "1 Test Lane",
            "city": "Istanbul",
            "zipCode": "34000",
        },
    }


@pytest.mark.django_db
def test_orders_get_requires_auth(api_client):
    response = api_client.get(reverse("orders"))
    assert response.status_code == 401


@pytest.mark.django_db
def test_orders_post_requires_auth(api_client, product):
    response = api_client.post(reverse("orders"), _payload(product), format="json")
    assert response.status_code == 401


@pytest.mark.django_db
def test_post_orders_creates_order_and_decrements_stock(auth_client, user, product):
    response = auth_client.post(reverse("orders"), _payload(product), format="json")
    assert response.status_code == 201
    body = response.json()
    assert "data" in body
    order_data = body["data"]
    assert order_data["status"] == "pending"
    assert order_data["totalPrice"] == 200.0
    assert order_data["items"][0]["productId"] == str(product.id)
    assert order_data["items"][0]["productName"] == product.name
    assert isinstance(order_data["id"], str)

    product.refresh_from_db()
    assert product.stock == 3
    assert Order.objects.filter(user=user).count() == 1


@pytest.mark.django_db
def test_post_orders_rejects_empty_items(auth_client, product):
    payload = _payload(product)
    payload["items"] = []
    response = auth_client.post(reverse("orders"), payload, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_my_orders_list_envelope(auth_client, user, product):
    auth_client.post(reverse("orders"), _payload(product), format="json")
    response = auth_client.get(reverse("orders"))
    assert response.status_code == 200
    body = response.json()
    assert body["meta"]["totalItems"] == 1
    assert body["data"][0]["status"] == "pending"
