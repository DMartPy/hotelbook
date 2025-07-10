from django.db import models


class HotelRoom(models.Model):
    id = models.AutoField(primary_key=True)

    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    date_create = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.description
