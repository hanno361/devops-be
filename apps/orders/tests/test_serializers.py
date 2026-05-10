import pytest
from apps.orders.serializers import CheckoutRequestSerializer

class TestCheckoutSerializers:
    def test_empty_items_list_raises_validation_error(self):
        payload = {
            "items": [], # Sepet boş!
            "shipping": {
                "name": "Test", "email": "test@test.local", 
                "address": "123", "city": "City"
            }
        }
        
        serializer = CheckoutRequestSerializer(data=payload)
        assert serializer.is_valid() is False
        assert "items" in serializer.errors
        assert "Items list cannot be empty." in str(serializer.errors["items"][0])