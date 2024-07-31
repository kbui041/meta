from django.urls import path
from .views import HomeView, HotelListView, HotelDetailView, RoomDetailView, BookingListView, BookingDetailView, AddReviewView, ReviewListView

# Define URL patterns for the application
urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Home page
    path('hotels/', HotelListView.as_view(), name='hotel_list'),  # List of hotels
    path('hotels/<int:hotel_id>/', HotelDetailView.as_view(), name='hotel_detail'),  # Hotel details page
    path('rooms/<int:room_id>/', RoomDetailView.as_view(), name='room_detail'),  # Room details page
    path('bookings/', BookingListView.as_view(), name='booking_list'),  # List of bookings
    path('bookings/<int:booking_id>/', BookingDetailView.as_view(), name='booking_detail'),  # Booking details page
    path('reviews/', ReviewListView.as_view(), name='review_list'),  # List of reviews
    path('reviews/add/<int:hotel_id>/', AddReviewView.as_view(), name='add_review'),  # Add a review page
]
