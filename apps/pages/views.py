from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.mixins import EnvelopeCreateMixin, EnvelopeRetrieveMixin

from .models import FAQ, AboutPage
from .serializers import AboutPageSerializer, ContactMessageSerializer, FAQSerializer


class FAQListView(generics.ListAPIView):
    serializer_class = FAQSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return FAQ.objects.filter(is_active=True)


class AboutPageView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AboutPageSerializer

    def get(self, request):
        about = AboutPage.objects.first()
        if not about:
            raise NotFound("About page not configured.")
        return Response({"data": AboutPageSerializer(about).data})


class ContactMessageCreateView(EnvelopeCreateMixin, generics.CreateAPIView):
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]
