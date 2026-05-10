import pytest
from apps.catalog.models import Category, Product
from apps.wishlist.serializers import WishlistItemSerializer

@pytest.fixture
def active_product(db):
    cat = Category.objects.create(name="Dizüstü Bilgisayar")
    return Product.objects.create(category=cat, name="MacBook Pro M3", price=75000.0, is_active=True)

@pytest.fixture
def inactive_product(db):
    cat = Category.objects.create(name="Telefon")
    # Belki de stoktan kalkmış eski bir model
    return Product.objects.create(category=cat, name="iPhone 11", price=20000.0, is_active=False)

@pytest.mark.django_db
class TestWishlistItemSerializer:
    def test_valid_product_id_deserialization(self, active_product):
        data = {"product_id": active_product.id}
        serializer = WishlistItemSerializer(data=data)
        
        assert serializer.is_valid() is True
        assert serializer.validated_data["product"] == active_product

    def test_cannot_add_inactive_product_to_wishlist(self, inactive_product):
        data = {"product_id": inactive_product.id}
        serializer = WishlistItemSerializer(data=data)
        
        assert serializer.is_valid() is False
        assert "product_id" in serializer.errors