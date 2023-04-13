from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView

# from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Vehicle, VehicleDetails
from .serializers import (
    VehicleDetailSerializer,
    VehicleSerializer,
    VehicleListSerializer,
)


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleDetailsViewSet(viewsets.ModelViewSet):
    queryset = VehicleDetails.objects.all()
    serializer_class = VehicleDetailSerializer


class OpenVehicleView(ListAPIView):
    queryset = Vehicle.objects.filter(is_active=True, on_trip=False)
    serializer_class = VehicleListSerializer


class VehicleDetailView(RetrieveAPIView):
    queryset = VehicleDetails.objects.filter(vehicle_main__is_active=True)
    serializer_class = VehicleDetailSerializer
    lookup_field = "vehicle_main__slug"


# x = ""
