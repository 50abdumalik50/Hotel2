from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from apps.rooms.api.serializers import RoomSerializer, RoomCreateSerializer
from apps.rooms.models import Room, Booking


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return RoomCreateSerializer
    elif self.action == 'retrieve':
        return RoomSerializer
    return self.serializer_class


class RoomUpdateDeleteRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# List and Create Room Views
# class RoomListCreateView(generics.ListCreateAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer


# Retrieve, Update and Delete Room Views
# class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer


# class BookingListCreateView(generics.ListCreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
#
#
# # Retrieve, Update and Delete Booking Views
# class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
