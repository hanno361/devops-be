import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from apps.catalog.models import Category, Product
from apps.orders.models import Order

User = get_user_model()

@pytest.fixture
def auth_client(db):
    user = User.objects.create_user(username="apiuser", email="api@test.local", password="pwd")
    client = APIClient()
    client.force_authenticate(user=user)
    return client, user

@pytest.fixture
def gpu_product(db):
    cat = Category.objects.create(name="Ekran Kartları")
    return Product.objects.create(category=cat, name="NVIDIA RTX 5090", price=85000.0, stock=10)

@pytest.mark.django_db
class TestOrderAPI:
    def test_checkout_endpoint(self, auth_client, gpu_product):
        client, user = auth_client
        payload = {
            "items": [
                {
                    "productId": str(gpu_product.id),
                    "productName": gpu_product.name,
                    "quantity": 1,
                    "price": 85000.0
                }
            ],
            "shipping": {
                "name": "Safa", "email": "api@test.local", 
                "address": "Kampüs", "city": "Sakarya"
            }
        }
        
        # POST isteği
        response = client.post("/api/orders", payload, format="json")
        assert response.status_code == 201
        
        data = response.json()["data"]
        assert data["totalPrice"] == 85000.0
        assert data["status"] == "pending" # Modeldeki varsayılan değer

    def test_get_order_detail(self, auth_client):
        client, user = auth_client
        
        # Test için manuel bir sipariş oluştur
        order = Order.objects.create(user=user, email=user.email, total=100.0)
        
        # Detail view 'number' field'ına göre arıyor
        response = client.get(f"/api/orders/{order.number}")
        
        assert response.status_code == 200
        assert response.json()["data"]["orderNumber"] == order.number
    
    def test_get_orders_list(self, auth_client):
        client, user = auth_client
        
        # Kullanıcı için 2 adet sahte sipariş oluştur
        Order.objects.create(user=user, email=user.email, total=1500.0)
        Order.objects.create(user=user, email=user.email, total=2500.0)
        
        # APPEND_SLASH=False olduğu için trailing slash YOK
        response = client.get("/api/orders")
        
        assert response.status_code == 200
        
        # List endpointleri "data" ve "meta" zarfı döner
        body = response.json()
        assert "data" in body
        assert "meta" in body
        assert len(body["data"]) == 2