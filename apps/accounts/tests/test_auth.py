import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


@pytest.mark.django_db
def test_register_returns_user_and_token(api_client):
    payload = {
        "email": "new@test.local",
        "password": "verystrongpass123",
        "name": "New User",
    }
    response = api_client.post(reverse("register"), payload, format="json")
    assert response.status_code == 201
    body = response.json()
    assert "token" in body
    assert body["user"]["email"] == "new@test.local"
    assert body["user"]["name"] == "New User"
    assert isinstance(body["user"]["id"], str)
    assert User.objects.filter(email="new@test.local").exists()


@pytest.mark.django_db
def test_register_rejects_duplicate_email(api_client, user):
    payload = {"email": user.email, "password": "verystrongpass123", "name": "Dup"}
    response = api_client.post(reverse("register"), payload, format="json")
    assert response.status_code == 400
    assert response.json()["error"]["code"]


@pytest.mark.django_db
def test_login_returns_user_and_token(api_client, user):
    response = api_client.post(
        reverse("login"),
        {"email": user.email, "password": "testpass123"},
        format="json",
    )
    assert response.status_code == 200
    body = response.json()
    assert "token" in body
    assert body["user"]["email"] == user.email


@pytest.mark.django_db
def test_login_rejects_bad_credentials(api_client, user):
    response = api_client.post(
        reverse("login"),
        {"email": user.email, "password": "wrong"},
        format="json",
    )
    assert response.status_code == 401
    assert response.json()["error"]["code"]


@pytest.mark.django_db
def test_me_requires_auth(api_client):
    response = api_client.get(reverse("me"))
    assert response.status_code == 401


@pytest.mark.django_db
def test_me_returns_enveloped_user(auth_client, user):
    response = auth_client.get(reverse("me"))
    assert response.status_code == 200
    body = response.json()
    assert body["data"]["email"] == user.email
    assert "name" in body["data"]
