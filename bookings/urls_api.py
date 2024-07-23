# bookings/urls_api.py

from django.urls import path
from . import views_api

urlpatterns = [
    path('hotels/', views_api.HotelListCreate.as_view(), name='api_hotel_list_create'),
    path('hotels/<int:pk>/', views_api.HotelDetail.as_view(), name='api_hotel_detail'),
    path('rooms/', views_api.RoomListCreate.as_view(), name='api_room_list_create'),
    path('rooms/<int:pk>/', views_api.RoomDetail.as_view(), name='api_room_detail'),
    path('bookings/', views_api.BookingListCreate.as_view(), name='api_booking_list_create'),
    path('bookings/<int:pk>/', views_api.BookingDetail.as_view(), name='api_booking_detail'),
    path('reviews/', views_api.ReviewListCreate.as_view(), name='api_review_list_create'),
    path('reviews/<int:pk>/', views_api.ReviewDetail.as_view(), name='api_review_detail'),
]
