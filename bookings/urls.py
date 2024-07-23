from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hotels/', views.hotel_list, name='hotel_list'),
    path('hotels/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('hotels/<int:hotel_id>/rooms/', views.room_list, name='room_list'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('bookings/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('hotels/<int:hotel_id>/add_review/', views.add_review, name='add_review'),
]
