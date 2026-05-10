import pytest
from django.contrib.admin.sites import AdminSite
from apps.pages.models import AboutPage
from apps.pages.admin import AboutPageAdmin


class MockRequest:
    """Admin metodunu taklit etmek için sahte request objesi."""
    pass


@pytest.mark.django_db
class TestAboutPageAdmin:
    def test_has_add_permission_singleton_logic(self):
        site = AdminSite()
        admin = AboutPageAdmin(AboutPage, site)
        request = MockRequest()

        # 1. Durum: Veritabanı boşken sayfa ekleme izni olmalı (True)
        assert admin.has_add_permission(request) is True

        # 2. Durum: Bir kayıt eklendikten sonra yeni sayfa ekleme izni kalkmalı (False)
        AboutPage.objects.create(title="Hakkımızda", intro="Test")
        assert admin.has_add_permission(request) is False