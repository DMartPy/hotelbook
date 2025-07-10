import pytest
from booking.serializer import BookingSerializer, BookingCreateSerializer
from booking.models import Booking


@pytest.mark.django_db
class TestBookingSerializer:
    def test_serialize_existing_booking(self, hotel_room_factory):
        """Тест сериализации существующего бронирования"""
        room = hotel_room_factory()
        booking = Booking.objects.create(
            room=room, start_booking="2025-01-01", end_booking="2025-01-02"
        )

        serializer = BookingSerializer(booking)
        data = serializer.data

        assert data["id"] == booking.id
        assert data["start_booking"] == "2025-01-01"
        assert data["end_booking"] == "2025-01-02"

    def test_serialize_multiple_bookings(self, hotel_room_factory):
        """Тест сериализации нескольких бронирований"""
        room = hotel_room_factory()
        booking1 = Booking.objects.create(
            room=room, start_booking="2025-01-01", end_booking="2025-01-02"
        )
        booking2 = Booking.objects.create(
            room=room, start_booking="2025-01-03", end_booking="2025-01-04"
        )

        serializer1 = BookingSerializer(booking1)
        serializer2 = BookingSerializer(booking2)

        assert serializer1.data["start_booking"] == "2025-01-01"
        assert serializer2.data["start_booking"] == "2025-01-03"
        assert serializer1.data["id"] != serializer2.data["id"]


@pytest.mark.django_db
class TestBookingCreateSerializer:
    def test_create_booking_valid_data(self, hotel_room_factory):
        """Тест создания бронирования с валидными данными"""
        room = hotel_room_factory()
        valid_data = {
            "room": room.id,
            "start_booking": "2025-01-01",
            "end_booking": "2025-01-02",
        }

        serializer = BookingCreateSerializer(data=valid_data)
        assert serializer.is_valid()

        booking = serializer.save()
        assert booking.room == room
        assert booking.start_booking.strftime("%Y-%m-%d") == "2025-01-01"
        assert booking.end_booking.strftime("%Y-%m-%d") == "2025-01-02"
        assert booking.is_active

    def test_create_booking_invalid_data(self, hotel_room_factory):
        """Тест создания бронирования с невалидными данными"""
        room = hotel_room_factory()
        invalid_data = {
            "room": room.id,
            "start_booking": "2025-01-02",  # дата окончания раньше начала
            "end_booking": "2025-01-01",
        }

        serializer = BookingCreateSerializer(data=invalid_data)
        assert not serializer.is_valid()
        # Проверяем, что есть ошибки валидации

    def test_create_booking_missing_fields(self, hotel_room_factory):
        """Тест создания бронирования с отсутствующими полями"""
        room = hotel_room_factory()
        incomplete_data = {
            "room": room.id,
            "start_booking": "2025-01-01"
            # нет поля end_booking
        }

        serializer = BookingCreateSerializer(data=incomplete_data)
        assert not serializer.is_valid()
        assert "end_booking" in serializer.errors

    def test_to_representation_returns_only_id(self, hotel_room_factory):
        """Тест метода to_representation - должен возвращать только ID"""
        room = hotel_room_factory()
        booking = Booking.objects.create(
            room=room, start_booking="2025-01-01", end_booking="2025-01-02"
        )

        serializer = BookingCreateSerializer(booking)
        assert serializer.data == {"id": booking.id}
        assert len(serializer.data) == 1
        assert "room" not in serializer.data
        assert "start_booking" not in serializer.data
        assert "end_booking" not in serializer.data

    def test_create_booking_with_invalid_room_id(self):
        """Тест создания бронирования с несуществующим ID комнаты"""
        invalid_data = {
            "room": 99999,  # несуществующий ID
            "start_booking": "2025-01-01",
            "end_booking": "2025-01-02",
        }

        serializer = BookingCreateSerializer(data=invalid_data)
        assert not serializer.is_valid()
        assert "room" in serializer.errors
