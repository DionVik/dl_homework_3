from django.test import TestCase
from .models import Category
from django.urls import reverse

class IndexViewTest(TestCase):

    def setUp(self):
        Category.objects.create(name='Animals')
    def test_index_view_url(self):
        response = self.client.get('/bulletin_board/')
        self.assertEqual(response.status_code, 200)

    def test_index_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
