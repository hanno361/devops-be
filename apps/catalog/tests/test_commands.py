import pytest
from django.core.management import call_command
from django.contrib.auth import get_user_model
from apps.catalog.models import Product, Category

User = get_user_model()

@pytest.mark.django_db
class TestSeedCommand:
    def test_seed_command_creates_demo_data(self):
        # Veritabanının boş olduğundan emin ol
        assert Product.objects.count() == 0
        
        # komutu çalıştır: python manage.py seed
        call_command("seed")
        
        # Seed içindeki PRODUCTS listesinde 10 adet ürün var
        assert Product.objects.count() == 10
        assert Category.objects.count() == 4
        assert User.objects.filter(email="admin@sinp.local").exists()

    def test_seed_command_with_reset_flag(self):
        # Önce sahte bir veri ekleyelim
        cat = Category.objects.create(name="Test Kategori")
        Product.objects.create(category=cat, name="Test Urun", sku="TEST", price=10)
        
        # --reset bayrağı ile komutu çalıştıralım
        call_command("seed", reset=True)
        
        # Test ürününün silinip, sadece seed datasının (10 ürün) kalmış olması gerekir
        assert Product.objects.count() == 10
        assert not Product.objects.filter(sku="TEST").exists()