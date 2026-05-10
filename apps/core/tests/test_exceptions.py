import pytest
from rest_framework.exceptions import ValidationError, NotFound, PermissionDenied
from apps.core.exceptions import envelope_exception_handler

class TestExceptionHandlers:
    def test_validation_error_formatting(self):
        exc = ValidationError({"email": ["Bu e-posta adresi zaten kullanılıyor."]})
        response = envelope_exception_handler(exc, context={})
        
        assert response.status_code == 400
        data = response.data
        
        assert "error" in data
        # DRF'in varsayılan hata kodu 'invalid'dir.
        assert data["error"]["code"] == "invalid"
        assert data["error"]["message"] == "Validation failed."
        assert data["error"]["details"]["email"] == ["Bu e-posta adresi zaten kullanılıyor."]

    def test_simple_api_exception_formatting(self):
        exc = NotFound("İstediğiniz ürün bulunamadı.")
        response = envelope_exception_handler(exc, context={})
        
        assert response.status_code == 404
        data = response.data
        
        assert data["error"]["code"] == "not_found"
        assert data["error"]["message"] == "İstediğiniz ürün bulunamadı."
        assert "details" not in data["error"]

    def test_list_type_error_formatting(self):
        exc = PermissionDenied(["Bu işlemi yapmaya yetkiniz yok."])
        response = envelope_exception_handler(exc, context={})
        
        assert response.status_code == 403
        data = response.data
        assert data["error"]["message"] == "Bu işlemi yapmaya yetkiniz yok."