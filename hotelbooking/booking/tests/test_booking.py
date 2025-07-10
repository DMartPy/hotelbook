from rest_framework.test import APIClient
from rest_framework import status
from booking.serializer import BookingSerializer
import pytest


@pytest.mark.django_db
def test_get_all_bookings(hotel_room_factory, booking_factory):
    url = "/api/v1/bookingslist/1"

    hotel_room = hotel_room_factory()
    book = booking_factory(room_id=hotel_room.id)

    client = APIClient()
    response = client.get(url)
    serializer = BookingSerializer(book).data
    assert response.status_code == status.HTTP_200_OK
    assert response.data["data"] == [serializer]


@pytest.mark.django_db
def test_create_booking(hotel_room_factory):
    url = "/api/v1/create_booking/"
    hotel_room = hotel_room_factory()

    book_data = {
        "room_id": hotel_room.id,
        "start_booking": "2025-01-01",
        "end_booking": "2025-01-02",
    }

    client = APIClient()
    response = client.post(url, data=book_data)
    assert response.status_code == status.HTTP_200_OK
