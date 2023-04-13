from .models import Vehicle, VehicleDetails
from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"


class VehicleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            "reg_no",
            "on_trip",
            "seats",
            "color_name",
            "color_code",
            "model_name",
            "model_manufacturer",
            "vehicle_image",
            "vehicle_owner",
            "vehicle_daily_price",
        ]


class VehicleDetailSerializer(serializers.ModelSerializer):
    vehicle_main = VehicleSerializer(read_only=True)

    class Meta:
        model = VehicleDetails
        fields = [
            "vehicle_main",
            "vehicle_verified",
        ]
        lookup_field = 'vehicle_main__slug'

