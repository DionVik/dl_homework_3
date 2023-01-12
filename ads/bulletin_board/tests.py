from django.test import TestCase
from .models import Category, Advertisement
from accounts.models import CustomUser
# Create your tests here.

class CategoryModelTest(TestCase):
    def setUp(self):
        Category.objects.create(name = "animals")

    def test_name(self):
        category_item = Category.objects.get(id=1)
        expected_category_name = f'{category_item.name}'
        self.assertEqual(expected_category_name, 'animals')


class AdvertisementModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        custom_user = CustomUser.objects.create(username='myusername',
                                               email='myemail@crazymail.com',
                                               password='mypassword',
                                               first_name='first_name',
                                               last_name='last_name',
                                               region='Togliatti')
        category = Category.objects.create(name = "animals")
        Advertisement.objects.create(author=custom_user,
                                     category=category,
                                     title="ad_title",
                                     content="Any ad content",
                                     price=50.00)

    def test_author(self):
        ad_item = Advertisement.objects.get(id=1)
        expected_ad_author_email = f'{ad_item.author.email}'
        self.assertEqual(expected_ad_author_email, 'myemail@crazymail.com')

    def test_category(self):
        ad_item = Advertisement.objects.get(id=1)
        expected_ad_category_name = f'{ad_item.category.name}'
        self.assertEqual(expected_ad_category_name, "animals")

    def test_title(self):
        ad_item = Advertisement.objects.get(id=1)
        expected_ad_title = f'{ad_item.title}'
        self.assertEqual(expected_ad_title, "ad_title")

    def test_content(self):
        ad_item = Advertisement.objects.get(id=1)
        expected_ad_content = f'{ad_item.content}'
        self.assertEqual(expected_ad_content, "Any ad content")

    def test_price(self):
        ad_item = Advertisement.objects.get(id=1)
        expected_ad_price = f'{ad_item.price}'
        self.assertEqual(expected_ad_price, '50.00')