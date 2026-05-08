from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import ContactMessage

class ContactTests(APITestCase):
    def test_create_contact_message(self):
        url = reverse('contact-create')
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Help Needed',
            'message': 'Please help me with my order.'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ContactMessage.objects.count(), 1)
