from rest_framework import viewsets
from rest_framework.response import Response
from .models import HotelRoom
from .serializer import HotelRoomCreateSerializer, HotelRoomSerializer


class HotelRoomAPI(viewsets.ModelViewSet):
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomSerializer

    def list(self, request, pk=None):
        """Сортировка по price и date_create /api/v1/roomslist/?ordering=-date_create"""

        if pk:
            rooms = HotelRoom.objects.order_by(pk)
        else:
            rooms = HotelRoom.objects.all()

        serializer = HotelRoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Принимает price и description, возвращает id"""

        serializer = HotelRoomCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        try:
            room = HotelRoom.objects.get(id=pk)
            room.delete()
            return Response(
                {"success": True, "message": f"Комната с ID {pk} успешно удалена"}
            )
        except HotelRoom.DoesNotExist:
            return Response(
                {"success": False, "message": f"Комната с ID {pk} не найдена"}
            )
