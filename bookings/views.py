# bookings/views.py

from django.shortcuts import render, get_object_or_404
from .models import Hotel, Room, Booking

def home(request):
    return render(request, 'bookings/home.html')

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'bookings/hotel_list.html', {'hotels': hotels})

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'bookings/hotel_detail.html', {'hotel': hotel})

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'bookings/room_list.html', {'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'bookings/room_detail.html', {'room': room})

def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})
