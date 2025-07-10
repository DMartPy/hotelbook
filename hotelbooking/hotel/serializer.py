from rest_framework import serializers
from .models import HotelRoom


class HotelRoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = ["description", "price"]

    def to_representation(self, instance):
        return {"id": instance.id}

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Цена не может быть отрицательной.")
        return value


class HotelRoomDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = ["id"]


class HotelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = "__all__"
