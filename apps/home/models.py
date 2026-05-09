from django.db import models


class HeroSlide(models.Model):
    bg = models.CharField(max_length=255, help_text="Background image URL or path")
    eyebrow = models.CharField(max_length=120, blank=True, default="")
    title = models.CharField(max_length=200)
    title_span = models.CharField(max_length=200, blank=True, default="")
    body = models.TextField(blank=True, default="")
    cta_label = models.CharField(max_length=80, default="Shop now")
    cta_href = models.CharField(max_length=255, default="/shop")
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("order", "id")

    def __str__(self) -> str:
        return self.title


class FeaturedProduct(models.Model):
    eyebrow = models.CharField(max_length=120, blank=True, default="")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    image_src = models.CharField(max_length=255)
    image_alt = models.CharField(max_length=200, blank=True, default="")
    cta_href = models.CharField(max_length=255, default="/shop")
    image_right = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("order", "id")

    def __str__(self) -> str:
        return self.title


class Banner(models.Model):
    """Singleton-style banner for the home page."""

    eyebrow = models.CharField(max_length=120, blank=True, default="")
    title = models.CharField(max_length=200)
    background_image = models.CharField(max_length=255)
    cta_label = models.CharField(max_length=80, default="Shop now")
    cta_href = models.CharField(max_length=255, default="/shop")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banner"

    def __str__(self) -> str:
        return self.title


class BannerFeature(models.Model):
    banner = models.ForeignKey(
        Banner, on_delete=models.CASCADE, related_name="features"
    )
    icon = models.CharField(max_length=80, help_text="Icon identifier or asset path")
    label = models.CharField(max_length=120)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ("order", "id")

    def __str__(self) -> str:
        return self.label
