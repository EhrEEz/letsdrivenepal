from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

from .models import User, SellerProfile


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token["role"] = user.role
        return token


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "phone_number",
            "first_name",
            "mid_name",
            "last_name",
            "email",
            "role",
            "dob",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        def validate_password(self, value: str) -> str:
            return make_password(value)

        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = (User,)
        fields = "__all__"
