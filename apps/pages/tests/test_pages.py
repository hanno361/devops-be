import pytest
from django.urls import reverse

from apps.pages.models import FAQ, ContactMessage


@pytest.mark.django_db
def test_faq_list_returns_active_only(api_client):
    FAQ.objects.create(question="Q1", answer="A1", is_active=True)
    FAQ.objects.create(question="Q2", answer="A2", is_active=False)
    response = api_client.get(reverse("faq-list"))
    assert response.status_code == 200
    questions = [f["question"] for f in response.json()]
    assert "Q1" in questions
    assert "Q2" not in questions


@pytest.mark.django_db
def test_contact_create_persists_message(api_client):
    payload = {
        "name": "Tester",
        "email": "tester@test.local",
        "subject": "Hi",
        "message": "Hello there",
    }
    response = api_client.post(reverse("contact-create"), payload, format="json")
    assert response.status_code == 201
    assert ContactMessage.objects.filter(email="tester@test.local").exists()
