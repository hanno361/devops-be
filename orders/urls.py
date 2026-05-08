from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddressViewSet, OrderViewSet, WishlistViewSet, CartViewSet

router = DefaultRouter()
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'wishlist', WishlistViewSet, basename='wishlist')
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
]
