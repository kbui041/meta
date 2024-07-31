from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import HotelViewSet, RoomViewSet, BookingViewSet, ReviewViewSet, CustomerViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'hotels', HotelViewSet)       # Register HotelViewSet with the URL prefix 'hotels'
router.register(r'rooms', RoomViewSet)         # Register RoomViewSet with the URL prefix 'rooms'
router.register(r'bookings', BookingViewSet)   # Register BookingViewSet with the URL prefix 'bookings'
router.register(r'reviews', ReviewViewSet)     # Register ReviewViewSet with the URL prefix 'reviews'
router.register(r'customers', CustomerViewSet) # Register CustomerViewSet with the URL prefix 'customers'

# Include the router URLs in the urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Include all the routes defined in the router
]
