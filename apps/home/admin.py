from django.contrib import admin

from .models import Banner, BannerFeature, FeaturedProduct, HeroSlide


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "theme", "order", "is_active")
    list_filter = ("theme",)
    list_editable = ("order", "is_active")


@admin.register(FeaturedProduct)
class FeaturedProductAdmin(admin.ModelAdmin):
    list_display = ("title", "theme", "order", "is_active")
    list_filter = ("theme",)
    list_editable = ("order", "is_active")


class BannerFeatureInline(admin.TabularInline):
    model = BannerFeature
    extra = 1


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "theme", "updated_at")
    list_filter = ("theme",)
    inlines = [BannerFeatureInline]
