# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User

# Internal:
from .models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProductViews(TestCase):
    """
    Class for testing the product views
    """

    def setUp(self):
        """
        This creates a test product
        """
        Product.objects.create(
            name='test_product',
            friendly_name='Test Product',
            price='10',
            sku='hj8001234567',
            description='This is a test description',
            has_sticker_finish=True,
        )

        User.objects.create_user(username='test_user',
                                 password='test_password')
        User.objects.create_superuser(
            username='test_superuser', password='test_password')

    def tearDown(self):
        """
        This deletes the test product
        """

    def test_get_all_products(self):
        """
        Tests getting the all products page
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_search_empty_query(self):
        """
        Tests searching without entering a query
        """
        response = self.client.get('/products/', {'q': ''})
        self.assertRedirects(response, '/products/')

    def test_product_search(self):
        """
        Test seraching for a product
        """
        response = self.client.get('/products/', {'q': 'test product'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_products_in_category_search(self):
        """
        Test searching for a category and returning all products in category
        """
        response = self.client.get('/products/', {'category': 'knits'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_show_product_detail(self):
        """
        Tests getting the product detail page for selected product
        """
        product = Product.objects.get()
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_add_product(self):
        """
        Tests adding a product 
        """
        self.client.login(username='test_superuser', password="test_password")
        response = self.client.post('/products/add/', {
            'name': 'test_product_2',
            'friendly_name': 'Test Product 2',
            'price': '10',
            'sku': 'hj8007654321',
            'description': 'This is a test description',
            'has_sticker_finish': False,
        })
        self.assertRedirects(response, '/products/2/')
