from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemReadSerializer(serializers.ModelSerializer):
    productId = serializers.SerializerMethodField()
    productName = serializers.CharField(source="product_name", read_only=True)
    price = serializers.FloatField(source="unit_price", read_only=True)

    class Meta:
        model = OrderItem
        fields = ("productId", "productName", "quantity", "price")

    def get_productId(self, obj):
        return str(obj.product_id) if obj.product_id else ""


class OrderReadSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    orderNumber = serializers.CharField(source="number", read_only=True)
    date = serializers.SerializerMethodField()
    totalPrice = serializers.FloatField(source="total", read_only=True)
    items = OrderItemReadSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ("id", "orderNumber", "date", "status", "totalPrice", "items")

    def get_id(self, obj):
        return str(obj.id)

    def get_date(self, obj):
        return obj.created_at.strftime("%d %B, %Y")


class CheckoutItemSerializer(serializers.Serializer):
    productId = serializers.CharField()
    productName = serializers.CharField()
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.FloatField(min_value=0)


class CheckoutShippingSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=32, required=False, allow_blank=True)
    address = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=120)
    zipCode = serializers.CharField(
        max_length=32, required=False, allow_blank=True
    )


class CheckoutRequestSerializer(serializers.Serializer):
    items = CheckoutItemSerializer(many=True)
    shipping = CheckoutShippingSerializer()

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Items list cannot be empty.")
        return value
