import pytest
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from apps.catalog.models import Category, Product
from apps.orders.services import create_order_from_payload

User = get_user_model()

@pytest.fixture
def customer(db):
    return User.objects.create_user(username="customer", email="cust@test.local", password="pwd")

@pytest.fixture
def android_test_device(db):
    cat = Category.objects.create(name="Geliştirici Cihazları")
    # Stok miktarını 5 olarak belirliyoruz
    return Product.objects.create(category=cat, name="Native Android Test Telefonu", price=25000.0, stock=5)

@pytest.mark.django_db
class TestOrderServices:
    def test_create_order_deducts_stock_successfully(self, customer, android_test_device):
        items_payload = [{
            "productId": str(android_test_device.id),
            "productName": android_test_device.name,
            "quantity": 2,
            "price": 25000.0
        }]
        shipping_payload = {
            "name": "Ahmet Safa", "email": "cust@test.local", 
            "address": "Teknokent", "city": "Sakarya"
        }

        order = create_order_from_payload(user=customer, items=items_payload, shipping=shipping_payload)
        
        # Siparişin başarıyla oluştuğunu doğrula
        assert order.total == 50000.0
        assert order.items.count() == 1
        
        # Stoktan 2 adet düşüldüğünü (5 - 2 = 3) doğrula
        android_test_device.refresh_from_db()
        assert android_test_device.stock == 3

    def test_create_order_fails_on_insufficient_stock(self, customer, android_test_device):
        items_payload = [{
            "productId": str(android_test_device.id),
            "productName": android_test_device.name,
            "quantity": 10, # Stokta 5 var, 10 istiyoruz!
            "price": 25000.0
        }]
        shipping_payload = {"name": "Ahmet", "email": "a@b.com", "address": "Adres", "city": "Şehir"}

        # ValidationError fırlatılmasını bekliyoruz
        with pytest.raises(ValidationError) as excinfo:
            create_order_from_payload(user=customer, items=items_payload, shipping=shipping_payload)
        
        assert "Insufficient stock" in str(excinfo.value)