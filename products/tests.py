from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Category, Product
from django.contrib.auth import get_user_model

User = get_user_model()

class ProductTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics', slug='electronics')
        self.product = Product.objects.create(
            category=self.category,
            name='Airpods',
            slug='airpods',
            description='Wireless earbuds',
            price='130.00',
            old_price='110.00'
        )
        self.admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin')

    def test_get_categories(self):
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Electronics')

    def test_get_products(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Airpods')

    def test_create_product_authenticated(self):
        self.client.force_authenticate(user=self.admin)
        data = {
            'category_id': self.category.id,
            'name': 'Smartwatch',
            'slug': 'smartwatch',
            'description': 'Smartwatch',
            'price': '250.00'
        }
        response = self.client.post(reverse('product-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_create_product_unauthenticated(self):
        data = {
            'category_id': self.category.id,
            'name': 'Drone',
            'slug': 'drone',
            'description': 'Drone',
            'price': '500.00'
        }
        response = self.client.post(reverse('product-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
