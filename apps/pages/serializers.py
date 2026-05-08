from rest_framework import serializers

from .models import FAQ, AboutPage, ContactMessage, TeamMember


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ("id", "question", "answer", "order")


class TeamMemberSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = TeamMember
        fields = ("id", "name", "role", "bio", "photo_url", "order")

    def get_photo_url(self, obj):
        if not obj.photo:
            return None
        request = self.context.get("request")
        return request.build_absolute_uri(obj.photo.url) if request else obj.photo.url


class AboutPageSerializer(serializers.ModelSerializer):
    cover_url = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()

    class Meta:
        model = AboutPage
        fields = ("id", "title", "intro", "body", "cover_url", "team", "updated_at")

    def get_cover_url(self, obj):
        if not obj.cover:
            return None
        request = self.context.get("request")
        return request.build_absolute_uri(obj.cover.url) if request else obj.cover.url

    def get_team(self, obj):
        return TeamMemberSerializer(
            TeamMember.objects.all(), many=True, context=self.context
        ).data


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ("id", "name", "email", "subject", "message", "created_at")
        read_only_fields = ("id", "created_at")
