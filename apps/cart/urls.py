from django.urls import path

from .views import CartClearView, CartItemAddView, CartItemUpdateDeleteView, MyCartView

urlpatterns = [
    path("", MyCartView.as_view(), name="my-cart"),
    path("items/", CartItemAddView.as_view(), name="cart-item-add"),
    path("items/<int:item_id>/", CartItemUpdateDeleteView.as_view(), name="cart-item-detail"),
    path("clear/", CartClearView.as_view(), name="cart-clear"),
]
