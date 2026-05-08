from rest_framework import serializers

from .models import Brand, Category, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "slug", "description", "product_count")


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name", "slug", "logo")


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("id", "image", "alt", "is_primary", "order")


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="slug", read_only=True)
    brand = serializers.SlugRelatedField(slug_field="slug", read_only=True)
    primary_image = serializers.SerializerMethodField()
    effective_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )
    is_on_sale = serializers.BooleanField(read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "slug",
            "short_description",
            "price",
            "sale_price",
            "effective_price",
            "is_on_sale",
            "stock",
            "is_featured",
            "category",
            "brand",
            "primary_image",
        )

    def get_primary_image(self, obj):
        primary = next((i for i in obj.images.all() if i.is_primary), None)
        if not primary:
            primary = obj.images.first() if obj.images.exists() else None
        if primary and primary.image:
            request = self.context.get("request")
            url = primary.image.url
            return request.build_absolute_uri(url) if request else url
        return None


class ProductDetailSerializer(ProductListSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta(ProductListSerializer.Meta):
        fields = ProductListSerializer.Meta.fields + ("description", "sku", "images")
