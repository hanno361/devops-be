import pytest
from apps.home.models import Banner, BannerFeature, FeaturedProduct, HeroSlide


@pytest.mark.django_db
class TestHomeModels:
    def test_heroslide_str_and_defaults(self):
        slide = HeroSlide.objects.create(
            title="Yapay Zeka Destekli İşlemciler", 
            bg="/images/cpu.jpg"
        )
        assert str(slide) == "Yapay Zeka Destekli İşlemciler"
        assert slide.is_active is True  # Varsayılan değer
        assert slide.cta_label == "Shop now"

    def test_featuredproduct_str(self):
        feat = FeaturedProduct.objects.create(
            title="Razer DeathAdder V3 Pro", 
            image_src="/img/mouse.png"
        )
        assert str(feat) == "Razer DeathAdder V3 Pro"

    def test_banner_and_feature_str(self):
        banner = Banner.objects.create(title="Geliştirici Günleri İndirimi")
        feature = BannerFeature.objects.create(banner=banner, label="Ücretsiz Kargo", icon="truck")
        
        assert str(banner) == "Geliştirici Günleri İndirimi"
        assert str(feature) == "Ücretsiz Kargo"