import pytest
from apps.pages.models import FAQ, AboutPage
from apps.pages.serializers import FAQSerializer, AboutPageSerializer


@pytest.mark.django_db
class TestFAQSerializer:
    def test_id_is_string(self):
        faq = FAQ.objects.create(question="Q", answer="A")
        serializer = FAQSerializer(faq)
        
        # Frontend kontratı gereği id string dönmeli
        assert isinstance(serializer.data["id"], str)
        assert serializer.data["id"] == str(faq.id)


@pytest.mark.django_db
class TestAboutPageSerializer:
    def test_get_body_returns_empty_list_when_no_body(self):
        about = AboutPage.objects.create(title="About")
        serializer = AboutPageSerializer(about)
        assert serializer.data["body"] == []

    def test_get_body_strips_whitespace_and_ignores_empty_lines(self):
        # Bilerek hatalı, bol boşluklu ve gereksiz yeni satır içeren bir metin
        raw_body = " İlk paragraf. \n\n \n\n İkinci paragraf. \n\n"
        about = AboutPage.objects.create(title="About", body=raw_body)
        serializer = AboutPageSerializer(about)
        
        expected = ["İlk paragraf.", "İkinci paragraf."]
        assert serializer.data["body"] == expected