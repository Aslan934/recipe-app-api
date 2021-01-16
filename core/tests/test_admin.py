from django.test import TestCase
from django.contrib.auth import get_user_model


class TestModels(TestCase):

    def test_create_user_with_email(self):
        """Test creating user with email and password is succesfull"""
        email = 'test@gmail.com'
        password = 'test1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that check if user email is normalized"""
        email = 'aslan@GMAIL.COM'
        password = 'aslan1234'
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, user.email.lower())

    def test_new_user_email_validation(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_new_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser('test@gmail.com', '123456')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
