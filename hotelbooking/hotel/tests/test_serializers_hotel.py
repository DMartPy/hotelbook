import pytest
from hotel.serializer import HotelRoomSerializer, HotelRoomCreateSerializer


@pytest.mark.django_db
class TestHotelRoomSerializer:
    def test_serialize_existing_room(self, hotel_room_factory):
        """Тест сериализации существующей комнаты"""
        room = hotel_room_factory(description="Test Room", price=1000)
        serializer = HotelRoomSerializer(room)
        data = serializer.data

        assert data["id"] == room.id
        assert data["description"] == "Test Room"
        assert data["price"] == "1000.00"
        assert data["is_active"] == True
        assert "date_create" in data

    def test_serialize_multiple_rooms(self, hotel_room_factory):
        """Тест сериализации нескольких комнат"""
        room1 = hotel_room_factory(description="Room 1", price=500)
        room2 = hotel_room_factory(description="Room 2", price=800)

        serializer1 = HotelRoomSerializer(room1)
        serializer2 = HotelRoomSerializer(room2)

        assert serializer1.data["description"] == "Room 1"
        assert serializer2.data["description"] == "Room 2"
        assert serializer1.data["id"] != serializer2.data["id"]


@pytest.mark.django_db
class TestHotelRoomCreateSerializer:
    def test_create_room_valid_data(self):
        """Тест создания комнаты с валидными данными"""
        valid_data = {"description": "New Room", "price": 1500}
        serializer = HotelRoomCreateSerializer(data=valid_data)

        assert serializer.is_valid()
        room = serializer.save()
        assert room.description == "New Room"
        assert float(room.price) == 1500
        assert room.is_active == True

    def test_create_room_invalid_data(self):
        """Тест создания комнаты с невалидными данными"""
        invalid_data = {"description": "", "price": -100}
        serializer = HotelRoomCreateSerializer(data=invalid_data)

        assert not serializer.is_valid()
        assert "description" in serializer.errors
        assert "price" in serializer.errors

    def test_to_representation_returns_only_id(self, hotel_room_factory):
        """Тест метода to_representation - должен возвращать только ID"""
        room = hotel_room_factory()
        serializer = HotelRoomCreateSerializer(room)

        assert serializer.data == {"id": room.id}
        assert len(serializer.data) == 1
        assert "description" not in serializer.data
        assert "price" not in serializer.data
