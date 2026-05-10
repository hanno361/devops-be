import pytest
from django.test import RequestFactory
from rest_framework.request import Request
from apps.core.pagination import EnvelopePagination

class TestEnvelopePagination:
    def test_pagination_meta_and_data_structure(self):
        factory = RequestFactory()
        django_request = factory.get("/?page=2&pageSize=5")
        # DRF Request sarmalaması
        drf_request = Request(django_request)
        
        paginator = EnvelopePagination()
        dummy_queryset = list(range(1, 21)) 
        
        # Artık paginator drf_request içindeki query_params'ı okuyabilecek
        paginated_data = paginator.paginate_queryset(dummy_queryset, drf_request)
        response = paginator.get_paginated_response(paginated_data)
        
        data = response.data
        
        assert "data" in data
        assert "meta" in data
        
        meta = data["meta"]
        assert meta["page"] == 2
        assert meta["pageSize"] == 5
        assert meta["totalItems"] == 20
        assert meta["totalPages"] == 4