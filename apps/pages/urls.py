from django.urls import path

from .views import AboutPageView, ContactMessageCreateView, FAQListView

urlpatterns = [
    path("faqs/", FAQListView.as_view(), name="faq-list"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactMessageCreateView.as_view(), name="contact-create"),
]
