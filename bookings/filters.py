import django_filters
from .models import Hotel, Room

# Filter class for the Hotel model
class HotelFilter(django_filters.FilterSet):
    class Meta:
        # Specify the model to filter
        model = Hotel
        # Define the fields to filter and their lookup types
        fields = {
            'name': ['icontains'],  # Search by name (case-insensitive)
            'city': ['exact'],      # Filter by city
            'country': ['exact'],   # Filter by country
        }

# Filter class for the Room model
class RoomFilter(django_filters.FilterSet):
    class Meta:
        # Specify the model to filter
        model = Room
        # Define the fields to filter and their lookup types
        fields = {
            'name': ['icontains'],  # Search by name (case-insensitive)
            'hotel': ['exact'],     # Filter by hotel
        }
