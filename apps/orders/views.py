from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Order
from .serializers import (
    CheckoutRequestSerializer,
    OrderReadSerializer,
)
from .services import create_order_from_payload


class OrderListCreateView(generics.ListCreateAPIView):
    """GET  /orders -> ApiListResponse<Order> (paginated)
    POST /orders -> ApiResponse<Order> (creates from payload).
    """

    serializer_class = OrderReadSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ("created_at", "total")
    ordering = ("-created_at",)

    def get_queryset(self):
        return (
            Order.objects.filter(user=self.request.user).prefetch_related("items")
        )

    def create(self, request, *args, **kwargs):
        serializer = CheckoutRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = create_order_from_payload(
            user=request.user,
            items=serializer.validated_data["items"],
            shipping=serializer.validated_data["shipping"],
        )
        return Response(
            {"data": OrderReadSerializer(order).data},
            status=status.HTTP_201_CREATED,
        )


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderReadSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "number"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related("items")

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response({"data": self.get_serializer(instance).data})
