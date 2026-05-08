from decimal import Decimal

from django.db import transaction
from rest_framework.exceptions import ValidationError

from apps.cart.models import Cart

from .models import Order, OrderItem

DEFAULT_SHIPPING_FEE = Decimal("9.99")


@transaction.atomic
def create_order_from_cart(*, user, address: dict, note: str = "") -> Order:
    """Convert the user's cart into a persisted Order, snapshotting product data.

    Validates stock and decrements it. Clears the cart on success.
    """
    cart = Cart.objects.select_for_update().filter(user=user).first()
    if not cart or not cart.items.exists():
        raise ValidationError("Cart is empty.")

    order = Order.objects.create(
        user=user,
        full_name=address["full_name"],
        email=address["email"],
        phone=address.get("phone", ""),
        address_line1=address["address_line1"],
        address_line2=address.get("address_line2", ""),
        city=address["city"],
        postal_code=address.get("postal_code", ""),
        country=address["country"],
        note=note,
        shipping_fee=DEFAULT_SHIPPING_FEE,
    )

    for item in cart.items.select_related("product"):
        product = item.product
        if product.stock < item.quantity:
            raise ValidationError(
                f"Insufficient stock for {product.name} (available: {product.stock})."
            )
        product.stock -= item.quantity
        product.save(update_fields=["stock"])
        OrderItem.objects.create(
            order=order,
            product=product,
            product_name=product.name,
            product_sku=product.sku,
            unit_price=product.effective_price,
            quantity=item.quantity,
        )

    order.recalculate_totals()
    cart.items.all().delete()
    return order
