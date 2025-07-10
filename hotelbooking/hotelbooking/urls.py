from django.contrib import admin
from django.urls import path
from hotel.views import HotelRoomAPI
from booking.views import BookingRoomAPI

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/roomslist/", HotelRoomAPI.as_view({"get": "list"})),
    path("api/v1/roomslist/<str:pk>", HotelRoomAPI.as_view({"get": "list"})),
    path("api/v1/create_room/", HotelRoomAPI.as_view({"post": "create"})),
    path("api/v1/delete_room/<int:pk>", HotelRoomAPI.as_view({"delete": "destroy"})),
    path("api/v1/bookingslist/<int:pk>", BookingRoomAPI.as_view({"get": "list"})),
    path("api/v1/create_booking/", BookingRoomAPI.as_view({"post": "create"})),
    path(
        "api/v1/delete_booking/<int:pk>", BookingRoomAPI.as_view({"delete": "destroy"})
    ),
]
