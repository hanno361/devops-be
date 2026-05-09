from decimal import Decimal

from django.db import transaction
from rest_framework.exceptions import ValidationError

from apps.catalog.models import Product

from .models import Order, OrderItem


@transaction.atomic
def create_order_from_payload(*, user, items: list[dict], shipping: dict) -> Order:
    """Persist an Order from the FE-shaped payload.

    items:    [{productId, productName, quantity, price}, ...]
    shipping: {name, email, phone, address, city, zipCode}
    """
    order = Order.objects.create(
        user=user,
        full_name=shipping["name"],
        email=shipping["email"],
        phone=shipping.get("phone", ""),
        address_line1=shipping["address"],
        city=shipping["city"],
        postal_code=shipping.get("zipCode", ""),
        country=shipping.get("country", ""),
    )

    for entry in items:
        product = None
        product_id_raw = str(entry["productId"])
        if product_id_raw.isdigit():
            product = (
                Product.objects.filter(pk=int(product_id_raw)).first()
            )
        if product is None:
            product = Product.objects.filter(slug=product_id_raw).first()

        quantity = entry["quantity"]
        if product is not None:
            if product.stock < quantity:
                raise ValidationError(
                    f"Insufficient stock for {product.name} (available: {product.stock})."
                )
            product.stock -= quantity
            product.save(update_fields=["stock"])

        OrderItem.objects.create(
            order=order,
            product=product,
            product_name=entry["productName"],
            product_sku=product.sku if product else "",
            unit_price=Decimal(str(entry["price"])),
            quantity=quantity,
        )

    order.recalculate_totals()
    return order
