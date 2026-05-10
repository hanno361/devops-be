import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
class TestUserManager:
    def test_create_user_success(self):
        user = User.objects.create_user(
            email="dev@test.local", 
            username="devuser", 
            password="StrongPassword123!"
        )
        assert user.email == "dev@test.local"
        assert user.username == "devuser"
        assert user.check_password("StrongPassword123!") is True
        assert user.is_staff is False

    def test_create_superuser_success(self):
        admin = User.objects.create_superuser(
            email="admin@test.local", 
            username="adminuser", 
            password="pwd"
        )
        assert admin.is_staff is True
        assert admin.is_superuser is True

    def test_missing_email_raises_error(self):
        with pytest.raises(ValueError, match="Email is required"):
            User.objects.create_user(email="", username="testuser", password="pwd")

    def test_missing_username_raises_error(self):
        with pytest.raises(ValueError, match="Username is required"):
            User.objects.create_user(email="test@test.local", username="", password="pwd")

    def test_user_str_representation(self):
        user = User.objects.create_user(email="safa@test.local", username="safa", password="pwd")
        assert str(user) == "safa@test.local"