from django.db.models import Prefetch
from rest_framework import generics, permissions

from apps.core.mixins import EnvelopeRetrieveMixin

from .models import Product, ProductImage
from .serializers import ProductSerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    search_fields = ("name", "short_description", "description", "sku")
    ordering_fields = ("price", "name", "created_at")
    ordering = ("-created_at",)

    def get_queryset(self):
        return (
            Product.objects.filter(is_active=True)
            .select_related("category", "brand")
            .prefetch_related(
                Prefetch(
                    "images",
                    queryset=ProductImage.objects.order_by("-is_primary", "order"),
                )
            )
        )


class ProductDetailView(EnvelopeRetrieveMixin, generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"

    def get_queryset(self):
        return (
            Product.objects.filter(is_active=True)
            .select_related("category", "brand")
            .prefetch_related("images")
        )
