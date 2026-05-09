from rest_framework import serializers

from .models import Brand, Category, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "name", "slug", "description")

    def get_id(self, obj) -> str:
        return str(obj.id)


class BrandSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = ("id", "name", "slug")

    def get_id(self, obj) -> str:
        return str(obj.id)


def _primary_image_url(obj, request):
    primary = next((i for i in obj.images.all() if i.is_primary), None)
    if not primary:
        primary = obj.images.first() if obj.images.exists() else None
    if primary and primary.image:
        url = primary.image.url
        return request.build_absolute_uri(url) if request else url
    return ""


def _badges(obj):
    badges = []
    if obj.is_on_sale:
        badges.append({"label": "Sale", "variant": "sale"})
        discount = int(round((1 - float(obj.sale_price) / float(obj.price)) * 100))
        if discount:
            badges.append({"label": f"-{discount}%", "variant": "default"})
    elif obj.is_featured:
        badges.append({"label": "New", "variant": "new"})
    return badges


class ProductSerializer(serializers.ModelSerializer):
    """FE-aligned Product shape: id is string, price is the effective price,
    originalPrice (camelCase) holds the strike-through value when on sale."""

    id = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    originalPrice = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    sold = serializers.SerializerMethodField()
    available = serializers.IntegerField(source="stock", read_only=True)
    badges = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "slug",
            "name",
            "price",
            "originalPrice",
            "image",
            "sold",
            "available",
            "badges",
            "description",
        )

    def get_id(self, obj) -> str:
        return str(obj.id)

    def get_price(self, obj) -> float:
        return float(obj.effective_price)

    def get_originalPrice(self, obj) -> float | None:
        return float(obj.price) if obj.is_on_sale else None

    def get_image(self, obj) -> str:
        if obj.image_url:
            return obj.image_url
        request = self.context.get("request")
        return _primary_image_url(obj, request)

    def get_sold(self, obj) -> int:
        return 0

    def get_badges(self, obj) -> list[dict]:
        return _badges(obj)
