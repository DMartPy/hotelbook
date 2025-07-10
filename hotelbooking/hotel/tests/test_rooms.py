from rest_framework.test import APIClient
from rest_framework import status
from hotel.models import HotelRoom
from hotel.serializer import HotelRoomSerializer
import pytest


@pytest.mark.django_db
def test_get_all_rooms(hotel_room_factory):
    url = "/api/v1/roomslist/"
    room = hotel_room_factory()

    client = APIClient()
    response = client.get(url)
    serializer = HotelRoomSerializer(room).data
    assert response.status_code == status.HTTP_200_OK
    assert response.data == [serializer]


@pytest.mark.django_db
def test_create_room():
    url = "/api/v1/create_room/"
    room_data = {"description": "Single", "price": 1000}

    client = APIClient()
    response = client.post(url, data=room_data)

    assert response.status_code == status.HTTP_200_OK

    room = HotelRoom.objects.get(id=response.data["id"])
    assert room.description == room_data["description"]
    assert float(room.price) == room_data["price"]
