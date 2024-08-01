from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Hotel, Room, Booking, Review, Customer
from .forms import ReviewForm, BookingForm
from django.core.exceptions import ValidationError

# View for adding a review
# views.py

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
            review.customer = request.user.customer
            review.hotel = hotel
            try:
                review.clean()
                review.save()
                return redirect('hotel_detail', hotel_id=hotel.id)
            except ValidationError as e:
                form.add_error(None, e)
        return render(request, 'bookings/add_review.html', {'form': form, 'hotel': hotel})

# View for the home page
class HomeView(View):
    def get(self, request):
        return render(request, 'bookings/home.html')

# View for the hotel list
class HotelListView(View):
    def get(self, request):
        hotels = Hotel.objects.all()
        return render(request, 'bookings/hotel_list.html', {'hotels': hotels})

# View for hotel details

# views.py

class HotelDetailView(View):
    def get(self, request, hotel_id):
        hotel = get_object_or_404(Hotel, pk=hotel_id)
        rooms = Room.objects.filter(hotel=hotel)
        reviews = Review.objects.filter(hotel=hotel)
        booking_form = BookingForm()
        return render(request, 'bookings/hotel_detail.html', {
            'hotel': hotel,
            'rooms': rooms,
            'reviews': reviews,
            'booking_form': booking_form
        })

    def post(self, request, hotel_id):
        hotel = get_object_or_404(Hotel, pk=hotel_id)
        rooms = Room.objects.filter(hotel=hotel)
        reviews = Review.objects.filter(hotel=hotel)
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.hotel = hotel
            booking.customer = request.user.customer
            booking.total_price = booking.room.price * (booking.check_out - booking.check_in).days
            booking.save()
            return redirect('booking_success', booking_id=booking.id)
        return render(request, 'bookings/hotel_detail.html', {
            'hotel': hotel,
            'rooms': rooms,
            'reviews': reviews,
            'booking_form': booking_form
        })



# View for room details
class RoomDetailView(View):
    def get(self, request, room_id):
        room = get_object_or_404(Room, pk=room_id)
        return render(request, 'bookings/room_detail.html', {'room': room})

# View for the booking list
class BookingListView(View):
    def get(self, request):
        bookings = Booking.objects.select_related('customer', 'room').all()
        return render(request, 'bookings/booking_list.html', {'bookings': bookings})

# View for booking details
class BookingDetailView(View):
    def get(self, request, booking_id):
        booking = get_object_or_404(Booking, pk=booking_id)
        return render(request, 'bookings/booking_detail.html', {'booking': booking})

# View for the review list
class ReviewListView(View):
    def get(self, request):
        reviews = Review.objects.all()
        return render(request, 'bookings/review_list.html', {'reviews': reviews})
