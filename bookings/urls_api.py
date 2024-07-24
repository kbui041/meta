from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import HotelViewSet, RoomViewSet, BookingViewSet, ReviewViewSet, CustomerViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
