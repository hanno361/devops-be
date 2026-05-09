from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """FE-aligned user shape: {id, email, name, avatarUrl?}."""

    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    avatarUrl = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "email", "name", "avatarUrl")

    def get_id(self, obj) -> str:
        return str(obj.id)

    def get_name(self, obj) -> str:
        full = f"{obj.first_name} {obj.last_name}".strip()
        return full or obj.username

    def get_avatarUrl(self, obj) -> str | None:
        return None


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True, validators=[validate_password]
    )
    name = serializers.CharField(max_length=200)

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email is already registered.")
        return value

    def create(self, validated_data):
        name = validated_data["name"].strip()
        first, _, last = name.partition(" ")
        username_base = validated_data["email"].split("@")[0]
        username = username_base
        suffix = 1
        while User.objects.filter(username=username).exists():
            suffix += 1
            username = f"{username_base}{suffix}"
        return User.objects.create_user(
            email=validated_data["email"],
            username=username,
            password=validated_data["password"],
            first_name=first,
            last_name=last,
        )
