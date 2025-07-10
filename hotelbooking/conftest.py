from hotel.models import HotelRoom
from booking.models import Booking
import pytest


@pytest.fixture
def hotel_room_factory():
    """Фабрика для создания комнат с разными параметрами"""

    def create_room(**kwargs):
        defaults = {"description": "Default Room", "price": 1000, "is_active": True}
        defaults.update(kwargs)  # переопределяем переданные параметры
        return HotelRoom.objects.create(**defaults)

    return create_room


@pytest.fixture
def booking_factory():
    """Фабрика для создания броней с разными параметрами"""

    def create_book(**kwargs):
        defaults = {
            "room_id": 1,
            "start_booking": "2025-01-01",
            "end_booking": "2025-01-02",
        }
        defaults.update(kwargs)  # переопределяем переданные параметры
        return Booking.objects.create(**defaults)

    return create_book
