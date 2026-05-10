import pytest
from django.contrib.auth import get_user_model
from apps.accounts.serializers import UserSerializer, RegisterSerializer

User = get_user_model()

@pytest.mark.django_db
class TestUserSerializer:
    def test_get_name_combines_first_and_last_name(self):
        user = User(first_name="Ahmet", last_name="Safa", username="ahmetsafa")
        serializer = UserSerializer(user)
        assert serializer.data["name"] == "Ahmet Safa"

    def test_get_name_falls_back_to_username(self):
        # İsim soyisim girilmemişse username dönmeli
        user = User(first_name="", last_name="", username="code_ninja")
        serializer = UserSerializer(user)
        assert serializer.data["name"] == "code_ninja"


@pytest.mark.django_db
class TestRegisterSerializer:
    def test_email_case_insensitive_unique_validation(self):
        User.objects.create_user(email="exist@test.local", username="exist", password="pwd")
        
        # Aynı mailin büyük harflisiyle kayıt olunmaya çalışılıyor
        data = {"email": "EXIST@test.local", "password": "Password123!", "name": "Test User"}
        serializer = RegisterSerializer(data=data)
        
        assert serializer.is_valid() is False
        assert "email" in serializer.errors

    def test_username_auto_generation_logic(self):
        # "dev" username'ine sahip iki kişi önceden kayıt olmuş olsun
        User.objects.create_user(email="other1@test.local", username="dev", password="pwd")
        User.objects.create_user(email="other2@test.local", username="dev2", password="pwd")

        # Şimdi prefix'i (email'in @'den önceki kısmı) "dev" olan yeni biri kayıt oluyor
        data = {
            "email": "dev@test.local",
            "password": "StrongPassword123!",
            "name": "Senior Developer"
        }
        
        serializer = RegisterSerializer(data=data)
        assert serializer.is_valid() is True
        user = serializer.save()

        # Serializer'daki while döngüsü sayesinde "dev3" üretilmiş olmalı
        assert user.username == "dev3"
        # İsim parçalama mantığı ("first_name", "last_name") doğru çalışmış mı?
        assert user.first_name == "Senior"
        assert user.last_name == "Developer"