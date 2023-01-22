from django.test import TestCase
from .models import CustomUser
# Create your tests here.

class CustomUserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(username='myusername',
                                email='myemail@crazymail.com',
                                password='mypassword',
                                first_name='first_name',
                                last_name='last_name')
    def test_username(self):
        user_item = CustomUser.objects.get(id=1)
        expected_data = user_item.username
        self.assertEqual(expected_data, 'myusername')

    def test_email(self):
        user_item = CustomUser.objects.get(id=1)
        expected_data = user_item.email
        self.assertEqual(expected_data, 'myemail@crazymail.com')
