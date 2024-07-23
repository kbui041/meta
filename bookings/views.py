from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, Room, Booking, Review
from .forms import ReviewForm

def home(request):
    return render(request, 'bookings/home.html')

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'bookings/hotel_list.html', {'hotels': hotels})

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'bookings/hotel_detail.html', {'hotel': hotel})

def room_list(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    rooms = hotel.room_set.all()
    return render(request, 'bookings/room_list.html', {'hotel': hotel, 'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'bookings/room_detail.html', {'room': room})

def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})

def add_review(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.hotel = hotel
            review.user = request.user
            review.save()
            return redirect('hotel_detail', hotel_id=hotel.id)
    else:
        form = ReviewForm()
    return render(request, 'bookings/add_review.html', {'form': form, 'hotel': hotel})
