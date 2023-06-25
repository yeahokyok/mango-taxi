from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class AuthenticationTest(APITestCase):
    def test_user_can_sign_up(self):
        response = self.client.post(
            reverse("sign_up"),
            data={
                "username": "user@example.com",
                "first_name": "Test",
                "last_name": "User",
                "password1": "testpassword",
                "password2": "testpassword",
            },
        )
        user = get_user_model().objects.last()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data["id"], user.id)
        self.assertEqual(response.data["username"], user.username)
        self.assertEqual(response.data["first_name"], user.first_name)
        self.assertEqual(response.data["last_name"], user.last_name)

    def test_user_cannot_sign_up_with_unmatched_passwords(self):
        response = self.client.post(
            reverse("sign_up"),
            data={
                "username": "testuser",
                "password1": "testpassword",
                "password2": "testpassword2",
            },
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(response.data, {"non_field_errors": ["Passwords must match."]})
