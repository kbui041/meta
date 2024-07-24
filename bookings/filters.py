import django_filters
from .models import Hotel, Room

class HotelFilter(django_filters.FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'name': ['icontains'],  # Search by name (case-insensitive)
            'city': ['exact'],      # Filter by city
            'country': ['exact'],   # Filter by country
        }

class RoomFilter(django_filters.FilterSet):
    class Meta:
        model = Room
        fields = {
            'name': ['icontains'],  # Search by name (case-insensitive)
            'hotel': ['exact'],     # Filter by hotel
        }
