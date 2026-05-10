import pytest
from apps.home.models import HeroSlide
from apps.home.serializers import HeroSlideSerializer

@pytest.mark.django_db
class TestHomeSerializers:
    def test_heroslide_cta_transformation(self):
        slide = HeroSlide.objects.create(
            title="MacBook Pro M3",
            bg="/macbook.png",
            cta_label="İncele",
            cta_href="/shop/macbook-m3"
        )
        
        serializer = HeroSlideSerializer(slide)
        data = serializer.data
        
        # Frontend'in beklediği cta objesi kontrolü
        assert "cta" in data
        assert isinstance(data["cta"], dict)
        assert data["cta"]["label"] == "İncele"
        assert data["cta"]["href"] == "/shop/macbook-m3"
        
        # ID'nin string döndüğünü doğrula
        assert isinstance(data["id"], str)