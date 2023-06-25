from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from accounts.serializers import UserSerializer
from trips.serializers import TripSerializer
from trips.models import Trip


class HttpTripTest(APITestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        response = self.client.post(
            reverse("login"),
            data={
                "username": user.username,
                "password": "testpassword",
            },
        )
        self.access = response.data["access"]

    def test_user_can_list_trips(self):
        trips = [
            Trip.objects.create(pick_up_address="A", drop_off_address="B"),
            Trip.objects.create(pick_up_address="B", drop_off_address="C"),
        ]
        response = self.client.get(
            reverse("trip:trip_list"), HTTP_AUTHORIZATION=f"Bearer {self.access}"
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        exp_trip_ids = [str(trip.id) for trip in trips]
        act_trip_ids = [trip.get("id") for trip in response.data]
        self.assertCountEqual(exp_trip_ids, act_trip_ids)
