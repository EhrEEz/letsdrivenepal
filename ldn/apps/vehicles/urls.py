from django.urls import path
from .viewsets import OpenVehicleView, VehicleDetailView

urlpatterns = [
    path("open-vehicles/", OpenVehicleView.as_view(), name="open-vehicles"),
    path(
        "vehicle/<slug:vehicle_main__slug>/",
        VehicleDetailView.as_view(),
        name="vehicle-detail",
    ),
]
