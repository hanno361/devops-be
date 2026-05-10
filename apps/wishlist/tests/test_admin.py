import pytest
from django.contrib import admin

from apps.wishlist.models import WishlistItem
from apps.wishlist.admin import WishlistItemAdmin


class TestWishlistItemAdmin:
    def test_admin_is_registered(self):
        #Modelin admin paneline başarılı bir şekilde kaydedildiği doğrulanır
        assert admin.site.is_registered(WishlistItem) is True

    def test_admin_configuration(self):
        #Admin sınıfının beklenen gösterim ve arama alanlarına sahip olduğu doğrulanır
        wishlist_admin = admin.site._registry[WishlistItem]
        
        assert wishlist_admin.list_display == ("user", "product", "created_at")
        assert wishlist_admin.search_fields == ("user__email", "product__name")