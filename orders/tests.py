from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from products.models import Category, Product
from .models import Address, Order, Wishlist, Cart

User = get_user_model()

class OrdersTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.force_authenticate(user=self.user)

        self.category = Category.objects.create(name='Cat1', slug='cat1')
        self.product = Product.objects.create(
            category=self.category, name='Product 1', slug='prod-1', price='10.00'
        )

    def test_address_crud(self):
        url = reverse('address-list')
        data = {
            'title': 'Home',
            'street': '123 Main St',
            'city': 'City',
            'state': 'State',
            'postal_code': '12345',
            'country': 'Country'
        }
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 1)

    def test_cart_add_item(self):
        url = reverse('cart-add-item')
        data = {'product_id': self.product.id, 'quantity': 2}
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.items.count(), 1)
        self.assertEqual(cart.items.first().quantity, 2)

    def test_wishlist_add_product(self):
        url = reverse('wishlist-add-product')
        data = {'product_id': self.product.id}
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        wishlist = Wishlist.objects.get(user=self.user)
        self.assertEqual(wishlist.products.count(), 1)

    def test_unauthenticated_access(self):
        self.client.logout()
        url = reverse('address-list')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
