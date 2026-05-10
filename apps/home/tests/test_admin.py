import pytest
from django.contrib.admin.sites import AdminSite
from apps.home.models import Banner
from apps.home.admin import BannerAdmin

class MockRequest:
    pass

@pytest.mark.django_db
class TestBannerAdmin:
    def test_has_add_permission_singleton_logic(self):
        site = AdminSite()
        admin_instance = BannerAdmin(Banner, site)
        request = MockRequest()

        # 1. Durum: Hiç banner yokken eklemeye izin vermeli (True)
        assert admin_instance.has_add_permission(request) is True

        # 2. Durum: Sistemde 1 tane banner varsa yenisine izin vermemeli (False)
        Banner.objects.create(title="Ana Sayfa Banner", background_image="bg.jpg")
        assert admin_instance.has_add_permission(request) is False