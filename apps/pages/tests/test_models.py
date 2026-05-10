import pytest
from apps.pages.models import FAQ, AboutPage, TeamMember, ContactMessage


@pytest.mark.django_db
class TestFAQModel:
    def test_str_representation(self):
        faq = FAQ.objects.create(question="Kargo ücreti ne kadar?", answer="Ücretsiz.")
        assert str(faq) == "Kargo ücreti ne kadar?"

    def test_default_values(self):
        faq = FAQ.objects.create(question="Test Soru", answer="Test Cevap")
        assert faq.order == 0
        assert faq.is_active is True


@pytest.mark.django_db
class TestAboutPageModel:
    def test_str_representation(self):
        about = AboutPage.objects.create(title="Hakkımızda?", intro="Atölyemiz...", body="Detaylar")
        assert str(about) == "Hakkımızda?"


@pytest.mark.django_db
class TestTeamMemberModel:
    def test_str_representation(self):
        member = TeamMember.objects.create(name="Ahmet Yılmaz", role="Kurucu")
        assert str(member) == "Ahmet Yılmaz — Kurucu"

    def test_ordering(self):
        TeamMember.objects.create(name="Üye 2", role="Rol", order=2)
        TeamMember.objects.create(name="Üye 1", role="Rol", order=1)
        
        # Meta sınıfındaki ordering=("order", "id") kuralına göre çekilmeli
        members = list(TeamMember.objects.all())
        assert members[0].name == "Üye 1"
        assert members[1].name == "Üye 2"


@pytest.mark.django_db
class TestContactMessageModel:
    def test_str_representation(self):
        msg = ContactMessage.objects.create(
            name="Ayşe", 
            email="ayse@example.com", 
            message="Merhaba"
        )
        assert str(msg) == "Ayşe <ayse@example.com>"

    def test_default_values(self):
        msg = ContactMessage.objects.create(
            name="Ayşe", 
            email="ayse@example.com", 
            message="Merhaba"
        )
        assert msg.is_read is False