from django.urls import path
from .views import home, hotel_list, hotel_detail, room_list, room_detail, booking_list, booking_detail, review_list
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('hotels/', hotel_list, name='hotel_list'),
    path('hotels/<int:hotel_id>/', hotel_detail, name='hotel_detail'),
    path('rooms/', room_list, name='room_list'),
    path('rooms/<int:room_id>/', room_detail, name='room_detail'),
    path('bookings/', booking_list, name='booking_list'),
    path('bookings/<int:booking_id>/', booking_detail, name='booking_detail'),
    path('reviews/', review_list, name='review_list'),
    path('hotels/<int:hotel_id>/add_review/', views.add_review, name = 'add_review')
]
