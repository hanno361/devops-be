import pytest
from decimal import Decimal
from django.contrib.auth import get_user_model

from apps.catalog.models import Category, Product
from apps.cart.models import Cart, CartItem

User = get_user_model()

@pytest.fixture
def test_user(db):
    return User.objects.create_user(email="dev@cart.local", username="cart_dev", password="pwd")

@pytest.fixture
def monitor(db):
    cat = Category.objects.create(name="Monitörler")
    # sku değerini "MON-001" olarak ekledik
    return Product.objects.create(
        category=cat, 
        name="32 inç 4K Yazılımcı Monitörü", 
        sku="MON-001", 
        price=15000.0
    )

@pytest.fixture
def keyboard(db):
    cat = Category.objects.create(name="Klavyeler")
    # sku değerini "KB-001" olarak ekledik
    return Product.objects.create(
        category=cat, 
        name="Mekanik Kodlama Klavyesi", 
        sku="KB-001", 
        price=3000.0
    )

@pytest.mark.django_db
class TestCartModels:
    def test_cart_calculations(self, test_user, monitor, keyboard):
        cart = Cart.objects.create(user=test_user)
        
        # 1 Monitör ve 2 Klavye ekleyelim
        CartItem.objects.create(cart=cart, product=monitor, quantity=1)
        CartItem.objects.create(cart=cart, product=keyboard, quantity=2)
        
        # Matematiksel doğrulama
        assert cart.item_count == 3
        # (1 * 15000) + (2 * 3000) = 21000
        assert cart.total == Decimal("21000.00")
        assert str(cart) == f"Cart of {test_user}"

    def test_cart_item_properties(self, test_user, monitor):
        cart = Cart.objects.create(user=test_user)
        item = CartItem.objects.create(cart=cart, product=monitor, quantity=3)
        
        assert item.unit_price == Decimal("15000.00")
        assert item.line_total == Decimal("45000.00")
        assert str(item) == "32 inç 4K Yazılımcı Monitörü x3"