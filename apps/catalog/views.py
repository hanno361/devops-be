from django.db.models import Count, Prefetch, Q
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.mixins import EnvelopeRetrieveMixin

from .models import (
    Category,
    Color,
    Product,
    ProductImage,
    Size,
    Tag,
    Theme,
    Vendor,
)
from .serializers import (
    CategorySerializer,
    ColorSerializer,
    ProductSerializer,
    SizeSerializer,
    TagSerializer,
    VendorSerializer,
)


# ─── Product list / detail ──────────────────────────────────────────────


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    search_fields = ("name", "short_description", "description", "sku")
    ordering_fields = ("price", "name", "created_at")
    ordering = ("-created_at",)

    def get_queryset(self):
        qs = (
            Product.objects.filter(is_active=True)
            .select_related("theme", "category", "brand", "vendor")
            .prefetch_related(
                Prefetch(
                    "images",
                    queryset=ProductImage.objects.order_by("-is_primary", "order"),
                )
            )
        )
        params = self.request.query_params

        theme = params.get("theme")
        if theme:
            qs = qs.filter(theme__slug=theme)

        category = params.get("category")
        if category:
            qs = qs.filter(category__slug=category)

        vendor = params.get("vendor")
        if vendor:
            qs = qs.filter(vendor__slug=vendor)

        color = params.get("color")
        if color:
            qs = qs.filter(colors__value=color)

        size = params.get("size")
        if size:
            qs = qs.filter(sizes__slug=size)

        tag = params.get("tag")
        if tag:
            qs = qs.filter(tags__slug=tag)

        return qs.distinct()


class ProductDetailView(EnvelopeRetrieveMixin, generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"

    def get_queryset(self):
        return (
            Product.objects.filter(is_active=True)
            .select_related("theme", "category", "brand", "vendor")
            .prefetch_related("images", "colors", "tags", "sizes")
        )


# ─── Sidebar endpoints (5 ayrı) ─────────────────────────────────────────


def _theme_filter(request) -> Q:
    """Common helper: if `?theme=` provided, restrict to that theme's products."""
    theme = request.query_params.get("theme")
    return Q(products__theme__slug=theme) if theme else Q()


class CategorySidebarView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def get_queryset(self):
        theme = self.request.query_params.get("theme")
        qs = Category.objects.all()
        if theme:
            qs = qs.filter(theme__slug=theme)
            count_filter = Q(products__is_active=True, products__theme__slug=theme)
        else:
            count_filter = Q(products__is_active=True)
        return qs.annotate(count=Count("products", filter=count_filter)).order_by("name")


class VendorSidebarView(generics.ListAPIView):
    serializer_class = VendorSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def get_queryset(self):
        theme = self.request.query_params.get("theme")
        count_filter = Q(products__is_active=True)
        qs = Vendor.objects.all()
        if theme:
            count_filter &= Q(products__theme__slug=theme)
            qs = qs.filter(products__theme__slug=theme).distinct()
        return qs.annotate(count=Count("products", filter=count_filter)).order_by("name")


class ColorSidebarView(generics.ListAPIView):
    serializer_class = ColorSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def get_queryset(self):
        theme = self.request.query_params.get("theme")
        qs = Color.objects.all()
        if theme:
            qs = qs.filter(products__theme__slug=theme).distinct()
        return qs.order_by("name")


class SizeSidebarView(generics.ListAPIView):
    serializer_class = SizeSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def get_queryset(self):
        theme = self.request.query_params.get("theme")
        qs = Size.objects.all()
        if theme:
            qs = qs.filter(products__theme__slug=theme).distinct()
        return qs.order_by("name")


class TagSidebarView(generics.ListAPIView):
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def get_queryset(self):
        theme = self.request.query_params.get("theme")
        qs = Tag.objects.all()
        if theme:
            qs = qs.filter(products__theme__slug=theme).distinct()
        return qs.order_by("name")
