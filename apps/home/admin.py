from django.contrib import admin

from .models import Banner, BannerFeature, FeaturedProduct, HeroSlide


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(FeaturedProduct)
class FeaturedProductAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")


class BannerFeatureInline(admin.TabularInline):
    model = BannerFeature
    extra = 1


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_at")
    inlines = [BannerFeatureInline]

    def has_add_permission(self, request):
        return not Banner.objects.exists()
