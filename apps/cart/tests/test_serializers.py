import pytest
from apps.catalog.models import Category, Product
from apps.cart.serializers import CartItemSerializer

@pytest.fixture
def active_product(db):
    cat = Category.objects.create(name="Aksesuarlar")
    return Product.objects.create(category=cat, name="Type-C Çoklayıcı", price=500.0,sku="CBL-001", is_active=True)

@pytest.mark.django_db
class TestCartSerializers:
    def test_quantity_must_be_at_least_one(self, active_product):
        # Miktarı 0 olarak göndermeyi deniyoruz
        data = {"product_id": active_product.id, "quantity": 0}
        serializer = CartItemSerializer(data=data)
        
        assert serializer.is_valid() is False
        assert "quantity" in serializer.errors
        assert "Quantity must be at least 1." in str(serializer.errors["quantity"][0])

    def test_valid_quantity_is_accepted(self, active_product):
        data = {"product_id": active_product.id, "quantity": 5}
        serializer = CartItemSerializer(data=data)
        
        assert serializer.is_valid() is True
        assert serializer.validated_data["quantity"] == 5