from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Hotel, Room, Booking, Review, Customer
from .serializers import HotelSerializer, RoomSerializer, BookingSerializer, ReviewSerializer, CustomerSerializer
from .filters import HotelFilter, RoomFilter

# ViewSet for the Hotel model
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()  # Define the queryset to be all Hotel objects
    serializer_class = HotelSerializer  # Specify the serializer to use
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # Enable filtering, searching, and ordering
    filterset_class = HotelFilter  # Specify the filter class to use
    search_fields = ['name', 'description']  # Define fields that can be searched
    ordering_fields = ['name', 'city', 'country']  # Define fields that can be used for ordering

# ViewSet for the Room model
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()  # Define the queryset to be all Room objects
    serializer_class = RoomSerializer  # Specify the serializer to use
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # Enable filtering, searching, and ordering
    filterset_class = RoomFilter  # Specify the filter class to use
    search_fields = ['name', 'hotel__name']  # Define fields that can be searched
    ordering_fields = ['name', 'price', 'hotel__name']  # Define fields that can be used for ordering

# ViewSet for the Booking model
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Define the queryset to be all Booking objects
    serializer_class = BookingSerializer  # Specify the serializer to use

# ViewSet for the Review model
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()  # Define the queryset to be all Review objects
    serializer_class = ReviewSerializer  # Specify the serializer to use

# ViewSet for the Customer model
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()  # Define the queryset to be all Customer objects
    serializer_class = CustomerSerializer  # Specify the serializer to use
