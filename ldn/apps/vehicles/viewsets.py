from rest_framework import viewsets

# from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Vehicle
from .serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
