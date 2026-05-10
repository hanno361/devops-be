import pytest
from django.db import IntegrityError
from django.contrib.auth import get_user_model

from apps.catalog.models import Category, Product
from apps.wishlist.models import WishlistItem

User = get_user_model()

@pytest.fixture
def test_user(db):
    # Eksik olan username eklendi
    return User.objects.create_user(username="testuser", email="user@test.com", password="password123")

@pytest.fixture
def test_product(db):
    category = Category.objects.create(name="Oyuncu Ekipmanları")
    return Product.objects.create(category=category, name="Mekanik Klavye", price=3500.0)

@pytest.mark.django_db
class TestWishlistItemModel:
    def test_str_representation(self, test_user, test_product):
        item = WishlistItem.objects.create(user=test_user, product=test_product)
        assert str(item) == f"{test_user} <3 {test_product}"

    def test_unique_together_constraint(self, test_user, test_product):
        WishlistItem.objects.create(user=test_user, product=test_product)
        
        with pytest.raises(IntegrityError):
            WishlistItem.objects.create(user=test_user, product=test_product)