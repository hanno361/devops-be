import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


@pytest.mark.django_db
def test_register_returns_tokens(api_client):
    url = reverse("register")
    payload = {
        "email": "new@test.local",
        "username": "newuser",
        "password": "verystrongpass123",
        "first_name": "New",
        "last_name": "User",
    }
    response = api_client.post(url, payload, format="json")
    assert response.status_code == 201
    body = response.json()
    assert "access" in body and "refresh" in body
    assert body["user"]["email"] == "new@test.local"
    assert User.objects.filter(email="new@test.local").exists()


@pytest.mark.django_db
def test_login_returns_jwt(api_client, user):
    url = reverse("login")
    response = api_client.post(
        url, {"email": user.email, "password": "testpass123"}, format="json"
    )
    assert response.status_code == 200
    assert "access" in response.json()


@pytest.mark.django_db
def test_me_requires_auth(api_client):
    response = api_client.get(reverse("me"))
    assert response.status_code == 401


@pytest.mark.django_db
def test_me_returns_current_user(auth_client, user):
    response = auth_client.get(reverse("me"))
    assert response.status_code == 200
    assert response.json()["email"] == user.email
