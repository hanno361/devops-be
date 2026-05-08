from django.db.models import Count, Prefetch
from rest_framework import filters, generics, permissions

from .models import Brand, Category, Product, ProductImage
from .serializers import (
    BrandSerializer,
    CategorySerializer,
    ProductDetailSerializer,
    ProductListSerializer,
)


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def get_queryset(self):
        return Category.objects.annotate(product_count=Count("products"))


class BrandListView(generics.ListAPIView):
    serializer_class = BrandSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None
    queryset = Brand.objects.all()


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = {
        "category__slug": ["exact"],
        "brand__slug": ["exact"],
        "is_featured": ["exact"],
        "price": ["gte", "lte"],
    }
    search_fields = ("name", "short_description", "description", "sku")
    ordering_fields = ("price", "created_at", "name")
    ordering = ("-created_at",)

    def get_queryset(self):
        return (
            Product.objects.filter(is_active=True)
            .select_related("category", "brand")
            .prefetch_related(
                Prefetch("images", queryset=ProductImage.objects.order_by("-is_primary", "order"))
            )
        )


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"

    def get_queryset(self):
        return (
            Product.objects.filter(is_active=True)
            .select_related("category", "brand")
            .prefetch_related("images")
        )
