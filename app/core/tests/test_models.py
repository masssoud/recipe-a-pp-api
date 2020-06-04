from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email(self):
        """Test creating user with email"""
        email = 'ma@gmail.com'
        password = '123456'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_invalid(self):
        """with no email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Sample test')

    def test_create_super_user(self):
        """Creating super user"""
        user = get_user_model().objects.create_superuser('test@email.com', 'Sample test')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)