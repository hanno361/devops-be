import pytest
from django.test import RequestFactory
from rest_framework.request import Request
from apps.core.filters import SortFilter

class MockView:
    ordering = ("-created_at",)

class TestSortFilter:
    def setup_method(self):
        self.factory = RequestFactory()
        self.view = MockView()
        self.filter_backend = SortFilter()

    def test_mapped_sort_value(self):
        django_request = self.factory.get("/?sort=price_desc")
        # Django request'ini DRF request'ine dönüştürüyoruz
        drf_request = Request(django_request)
        
        ordering = self.filter_backend.get_ordering(drf_request, None, self.view)
        assert ordering == ["-price"]

    def test_default_fallback_when_no_param(self):
        django_request = self.factory.get("/")
        drf_request = Request(django_request)
        
        ordering = self.filter_backend.get_ordering(drf_request, None, self.view)
        assert ordering == ("-created_at",)

    def test_default_fallback_when_invalid_param(self):
        django_request = self.factory.get("/?sort=hacker_siralama_123")
        drf_request = Request(django_request)
        
        ordering = self.filter_backend.get_ordering(drf_request, None, self.view)
        assert ordering == ("-created_at",)