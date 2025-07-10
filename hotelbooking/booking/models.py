from django.db import models
from hotel.models import HotelRoom


class Booking(models.Model):
    id = models.AutoField(primary_key=True)

    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    start_booking = models.DateField()
    end_booking = models.DateField()

    date_create = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Booking for room {self.room.id if self.room else 'deleted'}"
