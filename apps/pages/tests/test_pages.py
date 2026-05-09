import pytest
from django.urls import reverse

from apps.pages.models import FAQ, AboutPage, ContactMessage


@pytest.mark.django_db
def test_faq_list_envelope_and_active_only(api_client):
    FAQ.objects.create(question="Q1", answer="A1", is_active=True)
    FAQ.objects.create(question="Q2", answer="A2", is_active=False)
    response = api_client.get(reverse("faq-list"))
    assert response.status_code == 200
    body = response.json()
    assert "data" in body and "meta" in body
    questions = [f["question"] for f in body["data"]]
    assert "Q1" in questions
    assert "Q2" not in questions


@pytest.mark.django_db
def test_about_returns_body_as_string_array(api_client):
    AboutPage.objects.create(
        title="About",
        intro="An atelier.",
        body="First paragraph.\n\nSecond paragraph.\n\nThird.",
    )
    response = api_client.get(reverse("about"))
    assert response.status_code == 200
    body = response.json()["data"]
    assert isinstance(body["body"], list)
    assert len(body["body"]) == 3


@pytest.mark.django_db
def test_about_404_when_unconfigured(api_client):
    response = api_client.get(reverse("about"))
    assert response.status_code == 404
    assert response.json()["error"]["code"]


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
