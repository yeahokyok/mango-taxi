from rest_framework import viewsets, permissions

from .models import Trip
from .serializers import TripSerializer


class TripView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    lookup_field = "id"
    lookup_url_kwarg = "trip_id"
