import base64
import json
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
                "group": "rider",
            },
        )
        user = get_user_model().objects.last()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data["id"], user.id)
        self.assertEqual(response.data["username"], user.username)
        self.assertEqual(response.data["first_name"], user.first_name)
        self.assertEqual(response.data["last_name"], user.last_name)
        self.assertEqual(response.data["group"], user.group)

    def test_user_cannot_sign_up_with_unmatched_passwords(self):
        response = self.client.post(
            reverse("sign_up"),
            data={
                "username": "testuser",
                "password1": "testpassword",
                "password2": "testpassword2",
                "group": "rider",
            },
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(response.data, {"non_field_errors": ["Passwords must match."]})

    def test_user_cannot_sign_up_without_username(self):
        response = self.client.post(
            reverse("sign_up"),
            data={
                "password1": "testpassword",
                "password2": "testpassword",
                "group": "rider",
            },
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(response.data, {"username": ["This field is required."]})

    def test_user_cannot_sign_up_without_password(self):
        response = self.client.post(
            reverse("sign_up"),
            data={
                "username": "testuser",
            },
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual(response.data["password1"], ["This field is required."])
        self.assertEqual(response.data["password2"], ["This field is required."])

    def test_user_can_log_in(self):
        user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        response = self.client.post(
            reverse("login"),
            data={
                "username": "testuser",
                "password": "testpassword",
            },
        )
        # Parse payload data from access token.
        access = response.data["access"]
        header, payload, signature = access.split(".")
        decoded_payload = base64.b64decode(f"{payload}==")
        payload_data = json.loads(decoded_payload)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIsNotNone(response.data["refresh"])
        self.assertEqual(payload_data["id"], user.id)
        self.assertEqual(payload_data["username"], user.username)
        self.assertEqual(payload_data["first_name"], user.first_name)
        self.assertEqual(payload_data["last_name"], user.last_name)
