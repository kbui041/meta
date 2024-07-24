from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Hotel, Room, Booking, Review, Customer
from .forms import ReviewForm

class AddReviewView(View):
    def get(self, request, hotel_id):
        hotel = get_object_or_404(Hotel, pk=hotel_id)
        form = ReviewForm()
        return render(request, 'bookings/add_review.html', {'form': form, 'hotel': hotel})

    def post(self, request, hotel_id):
        hotel = get_object_or_404(Hotel, pk=hotel_id)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            customer, created = Customer.objects.get_or_create(user=request.user)
            review.customer = customer
            review.hotel = hotel
            review.save()
            return redirect('hotel_detail', hotel_id=hotel.id)
        return render(request, 'bookings/add_review.html', {'form': form, 'hotel': hotel})

class HomeView(View):
    def get(self, request):
        return render(request, 'bookings/home.html')

class HotelListView(View):
    def get(self, request):
        hotels = Hotel.objects.all()
        return render(request, 'bookings/hotel_list.html', {'hotels': hotels})

class HotelDetailView(View):
    def get(self, request, hotel_id):
        hotel = get_object_or_404(Hotel, pk=hotel_id)
        rooms = Room.objects.filter(hotel=hotel)
        reviews = Review.objects.filter(hotel=hotel)
        return render(request, 'bookings/hotel_detail.html', {
            'hotel': hotel,
            'rooms': rooms,
            'reviews': reviews
        })

class RoomDetailView(View):
    def get(self, request, room_id):
        room = get_object_or_404(Room, pk=room_id)
        return render(request, 'bookings/room_detail.html', {'room': room})

class BookingListView(View):
    def get(self, request):
        bookings = Booking.objects.select_related('customer', 'room').all()
        return render(request, 'bookings/booking_list.html', {'bookings': bookings})

class BookingDetailView(View):
    def get(self, request, booking_id):
        booking = get_object_or_404(Booking, pk=booking_id)
        return render(request, 'bookings/booking_detail.html', {'booking': booking})

class ReviewListView(View):
    def get(self, request):
        reviews = Review.objects.all()
        return render(request, 'bookings/review_list.html', {'reviews': reviews})
