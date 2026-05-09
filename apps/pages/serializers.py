from rest_framework import serializers

from .models import FAQ, AboutPage, ContactMessage


class FAQSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ("id", "question", "answer")

    def get_id(self, obj):
        return str(obj.id)


class AboutPageSerializer(serializers.ModelSerializer):
    body = serializers.SerializerMethodField()

    class Meta:
        model = AboutPage
        fields = ("title", "intro", "body")

    def get_body(self, obj):
        if not obj.body:
            return []
        return [p.strip() for p in obj.body.split("\n\n") if p.strip()]


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ("name", "email", "subject", "message")
