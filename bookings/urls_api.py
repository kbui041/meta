from django.urls import path, include
from . import views
from .views_api import (
    HotelListCreate,
    HotelDetail,
    RoomListCreate,
    RoomDetail,
    BookingListCreate,
    BookingDetail,
    ReviewListCreate,
    ReviewDetail,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('hotels/', HotelListCreate.as_view(), name='api_hotel_list_create'),
    path('hotels/<int:pk>/', HotelDetail.as_view(), name='api_hotel_detail'),
    path('rooms/', RoomListCreate.as_view(), name='api_room_list_create'),
    path('rooms/<int:pk>/', RoomDetail.as_view(), name='api_room_detail'),
    path('bookings/', BookingListCreate.as_view(), name='api_booking_list_create'),
    path('bookings/<int:pk>/', BookingDetail.as_view(), name='api_booking_detail'),
    path('reviews/', ReviewListCreate.as_view(), name='api_review_list_create'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='api_review_detail'),
]
