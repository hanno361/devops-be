from django.db import models
from django.utils.text import slugify


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugifiedNameModel(TimeStampedModel):
    """Reusable base for `(name, slug)` lookup tables."""

    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    class Meta:
        abstract = True
        ordering = ("name",)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Theme(SlugifiedNameModel):
    """Top-level grouping shown on the homepage (airpod, smartwatch, drone, backpack)."""


class Category(SlugifiedNameModel):
    # Override `name` from the base to drop its unique constraint —
    # category names like "Accessories" are intentionally reused across themes,
    # uniqueness is enforced on (theme, name) and on the slug.
    name = models.CharField(max_length=120)
    theme = models.ForeignKey(
        Theme,
        on_delete=models.PROTECT,
        related_name="categories",
        null=True,
        blank=True,
    )
    description = models.TextField(blank=True, default="")

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "categories"
        unique_together = (("theme", "name"),)


class Brand(SlugifiedNameModel):
    logo = models.ImageField(upload_to="brands/", blank=True, null=True)


class Vendor(SlugifiedNameModel):
    """Product vendor / manufacturer for the shop sidebar filter."""


class Tag(SlugifiedNameModel):
    """Product tag (New, Sale, Tech, Audio, ...)."""


class Size(SlugifiedNameModel):
    """Optional sizing for backpacks/apparel."""


class Color(TimeStampedModel):
    name = models.CharField(max_length=40, unique=True)
    value = models.SlugField(max_length=40, unique=True, blank=True)
    hex = models.CharField(max_length=7, default="#000000")

    class Meta:
        ordering = ("name",)

    def save(self, *args, **kwargs):
        if not self.value:
            self.value = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Product(TimeStampedModel):
    theme = models.ForeignKey(
        Theme,
        on_delete=models.PROTECT,
        related_name="products",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products"
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )
    colors = models.ManyToManyField(Color, blank=True, related_name="products")
    tags = models.ManyToManyField(Tag, blank=True, related_name="products")
    sizes = models.ManyToManyField(Size, blank=True, related_name="products")
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    short_description = models.CharField(max_length=300, blank=True, default="")
    description = models.TextField(blank=True, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    sku = models.CharField(max_length=64, unique=True)
    stock = models.PositiveIntegerField(default=0)
    image_url = models.CharField(
        max_length=255,
        blank=True,
        default="",
        help_text="External or static path to a primary image (e.g. /images/product1.webp).",
    )
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at",)
        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["is_active", "is_featured"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def effective_price(self):
        return self.sale_price if self.sale_price else self.price

    @property
    def is_on_sale(self) -> bool:
        return self.sale_price is not None and self.sale_price < self.price

    def __str__(self) -> str:
        return self.name


class ProductImage(TimeStampedModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="products/")
    alt = models.CharField(max_length=200, blank=True, default="")
    is_primary = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ("-is_primary", "order")

    def __str__(self) -> str:
        return f"{self.product.name} image"
