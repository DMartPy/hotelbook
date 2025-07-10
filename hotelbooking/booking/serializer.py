from rest_framework import serializers
from .models import Booking


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["room", "start_booking", "end_booking"]

    def to_representation(self, instance):
        return {"id": instance.id}

    def validate(self, data):
        start = data.get("start_booking")
        end = data.get("end_booking")
        if start and end and start > end:
            raise serializers.ValidationError(
                "Дата начала бронирования должна быть раньше даты окончания."
            )
        return data


class BookingDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "start_booking", "end_booking"]
