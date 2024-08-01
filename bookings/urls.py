# bookings/urls.py (application-level)

from django.urls import path
from .views import HomeView, HotelListView, HotelDetailView, RoomDetailView, BookingListView, BookingDetailView, ReviewListView, AddReviewView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('hotels/', HotelListView.as_view(), name='hotel_list'),
    path('hotel/<int:hotel_id>/', HotelDetailView.as_view(), name='hotel_detail'),
    path('room/<int:room_id>/', RoomDetailView.as_view(), name='room_detail'),
    path('bookings/', BookingListView.as_view(), name='booking_list'),
    path('booking/<int:booking_id>/', BookingDetailView.as_view(), name='booking_detail'),
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('hotel/<int:hotel_id>/add_review/', AddReviewView.as_view(), name='add_review'),
    path('booking_success/<int:booking_id>/', BookingDetailView.as_view(), name='booking_success'),
]
