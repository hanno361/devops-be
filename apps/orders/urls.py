from django.urls import path

from .views import CheckoutView, MyOrderDetailView, MyOrderListView

urlpatterns = [
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("", MyOrderListView.as_view(), name="my-orders"),
    path("<str:number>/", MyOrderDetailView.as_view(), name="my-order-detail"),
]
