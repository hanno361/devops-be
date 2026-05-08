from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound

from .models import FAQ, AboutPage, ContactMessage
from .serializers import AboutPageSerializer, ContactMessageSerializer, FAQSerializer


class FAQListView(generics.ListAPIView):
    serializer_class = FAQSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def get_queryset(self):
        return FAQ.objects.filter(is_active=True)


class AboutPageView(generics.RetrieveAPIView):
    serializer_class = AboutPageSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        about = AboutPage.objects.first()
        if not about:
            raise NotFound("About page not configured.")
        return about


class ContactMessageCreateView(generics.CreateAPIView):
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]
    queryset = ContactMessage.objects.all()
