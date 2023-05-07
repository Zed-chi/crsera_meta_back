from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from restaurant.models import Booking, Menu
from restaurant.api.serializers import (
    BookingSerializer,
    MenuItemSerializer,
)


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(
    generics.RetrieveUpdateAPIView, generics.DestroyAPIView
):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
