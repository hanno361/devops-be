import uuid
from decimal import Decimal

from django.conf import settings
from django.db import models

from apps.catalog.models import Product


class Order(models.Model):
    PENDING, PAID, SHIPPED, DELIVERED, CANCELLED = (
        "pending", "paid", "shipped", "delivered", "cancelled"
    )
    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (PAID, "Paid"),
        (SHIPPED, "Shipped"),
        (DELIVERED, "Delivered"),
        (CANCELLED, "Cancelled"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="orders"
    )
    number = models.CharField(max_length=32, unique=True, editable=False)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=PENDING)

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=32, blank=True, default="")
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, default="")
    city = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=32, blank=True, default="")
    country = models.CharField(max_length=120)

    note = models.TextField(blank=True, default="")
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    total = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def save(self, *args, **kwargs):
        if not self.number:
            self.number = uuid.uuid4().hex[:12].upper()
        super().save(*args, **kwargs)

    def recalculate_totals(self):
        self.subtotal = sum(
            (item.line_total for item in self.items.all()), Decimal("0.00")
        )
        self.total = self.subtotal + self.shipping_fee
        self.save(update_fields=["subtotal", "total", "updated_at"])

    def __str__(self) -> str:
        return f"Order {self.number}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    product_name = models.CharField(max_length=200)
    product_sku = models.CharField(max_length=64)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    @property
    def line_total(self) -> Decimal:
        return self.unit_price * self.quantity

    def __str__(self) -> str:
        return f"{self.product_name} x{self.quantity}"
