from django.urls import path
from .views import HomeView, HotelListView, HotelDetailView, RoomDetailView, BookingListView, BookingDetailView, AddReviewView, ReviewListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('hotels/', HotelListView.as_view(), name='hotel_list'),
    path('hotels/<int:hotel_id>/', HotelDetailView.as_view(), name='hotel_detail'),
    path('rooms/<int:room_id>/', RoomDetailView.as_view(), name='room_detail'),
    path('bookings/', BookingListView.as_view(), name='booking_list'),
    path('bookings/<int:booking_id>/', BookingDetailView.as_view(), name='booking_detail'),
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('reviews/add/<int:hotel_id>/', AddReviewView.as_view(), name='add_review'),
]
