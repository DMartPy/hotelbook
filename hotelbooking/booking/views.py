from rest_framework import viewsets
from rest_framework.response import Response
from booking.models import Booking
from booking.serializer import BookingCreateSerializer, BookingSerializer


class BookingRoomAPI(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request, pk=None):
        try:
            bookings = Booking.objects.filter(room_id=pk).order_by("start_booking")
            serializer = BookingSerializer(bookings, many=True)
            return Response(
                {
                    "success": True,
                    "message": f"Бронирования для комнаты с ID {pk} успешно получены",
                    "data": serializer.data,
                }
            )
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": f"Комната с ID {pk} не найдена. Ошибка: {e}",
                }
            )

    def create(self, request):
        """Принимает id комнаты, дату начала и окончания брони"""

        serializer = BookingCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        try:
            room = Booking.objects.get(id=pk)
            room.delete()
            return Response(
                {"success": True, "message": f"Бронь с ID {pk} успешно удалена"}
            )
        except Booking.DoesNotExist:
            return Response(
                {"success": False, "message": f"Бронь с ID {pk} не найдена"}
            )
