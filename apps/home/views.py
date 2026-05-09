from django.db.models import Prefetch
from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.blog.models import BlogPost
from apps.blog.serializers import BlogPostSerializer
from apps.catalog.models import Product, ProductImage
from apps.catalog.serializers import ProductSerializer

from .models import Banner, FeaturedProduct, HeroSlide
from .serializers import (
    BannerSerializer,
    FeaturedProductSerializer,
    HeroSlideSerializer,
)


class HeroSlideListView(generics.ListAPIView):
    serializer_class = HeroSlideSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return HeroSlide.objects.filter(is_active=True)


class FeaturedProductListView(generics.ListAPIView):
    serializer_class = FeaturedProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return FeaturedProduct.objects.filter(is_active=True)


class BannerView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        banner = Banner.objects.prefetch_related("features").first()
        if not banner:
            raise NotFound("Banner not configured.")
        return Response({"data": BannerSerializer(banner).data})


class HomeProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return (
            Product.objects.filter(is_active=True, is_featured=True)
            .select_related("category", "brand")
            .prefetch_related(
                Prefetch(
                    "images",
                    queryset=ProductImage.objects.order_by("-is_primary", "order"),
                )
            )
        )


class HomeBlogView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return (
            BlogPost.objects.filter(status=BlogPost.PUBLISHED)
            .order_by("-published_at")
        )
