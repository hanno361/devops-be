from rest_framework import serializers

from .models import Banner, BannerFeature, FeaturedProduct, HeroSlide


class HeroSlideSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    titleSpan = serializers.CharField(source="title_span", read_only=True)
    cta = serializers.SerializerMethodField()

    class Meta:
        model = HeroSlide
        fields = ("id", "bg", "eyebrow", "title", "titleSpan", "body", "cta")

    def get_id(self, obj) -> str:
        return str(obj.id)

    def get_cta(self, obj) -> dict:
        return {"label": obj.cta_label, "href": obj.cta_href}


class FeaturedProductSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    imageSrc = serializers.CharField(source="image_src", read_only=True)
    imageAlt = serializers.CharField(source="image_alt", read_only=True)
    ctaHref = serializers.CharField(source="cta_href", read_only=True)
    imageRight = serializers.BooleanField(source="image_right", read_only=True)

    class Meta:
        model = FeaturedProduct
        fields = (
            "id",
            "eyebrow",
            "title",
            "description",
            "imageSrc",
            "imageAlt",
            "ctaHref",
            "imageRight",
        )

    def get_id(self, obj) -> str:
        return str(obj.id)


class BannerFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerFeature
        fields = ("icon", "label")


class BannerSerializer(serializers.ModelSerializer):
    backgroundImage = serializers.CharField(source="background_image", read_only=True)
    ctaLabel = serializers.CharField(source="cta_label", read_only=True)
    ctaHref = serializers.CharField(source="cta_href", read_only=True)
    features = BannerFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Banner
        fields = (
            "eyebrow",
            "title",
            "backgroundImage",
            "features",
            "ctaLabel",
            "ctaHref",
        )
