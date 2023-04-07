from rest_framework import routers
from apps.vehicles import viewsets as vehicle_rental_views

router = routers.DefaultRouter()
router.register(r"Vehicle", vehicle_rental_views.VehicleViewSet)
