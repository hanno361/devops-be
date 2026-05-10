import pytest
from decimal import Decimal
from apps.catalog.models import Category, Product
from apps.catalog.serializers import ProductSerializer

@pytest.fixture
def category(db):
    return Category.objects.create(name="Yazilim Araclari")

@pytest.mark.django_db
class TestProductSerializer:
    def test_product_with_sale_generates_correct_badges_and_prices(self, category):
        # 1000 TL'lik ürün 800 TL'ye düşmüş (%20 indirim)
        product = Product.objects.create(
            category=category, name="IDE Lisansi", sku="IDE-1",
            price=Decimal("1000.00"), sale_price=Decimal("800.00")
        )
        
        serializer = ProductSerializer(product)
        data = serializer.data
        
        # Fiyat kontrolleri
        assert data["price"] == 800.0
        assert data["originalPrice"] == 1000.0
        
        # Badge kontrolleri
        badges = data["badges"]
        assert len(badges) == 2
        assert badges[0]["label"] == "Sale"
        assert badges[1]["label"] == "-20%"

    def test_featured_product_generates_new_badge(self, category):
        product = Product.objects.create(
            category=category, name="Yeni API Paketi", sku="API-1",
            price=Decimal("500.00"), is_featured=True
        )
        
        serializer = ProductSerializer(product)
        badges = serializer.data["badges"]
        
        assert len(badges) == 1
        assert badges[0]["label"] == "New"
        assert badges[0]["variant"] == "new"