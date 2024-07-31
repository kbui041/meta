from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Hotel, Room, Booking, Review, Customer
from .forms import ReviewForm

# View for adding a review
class AddReviewView(View):
    # Handle GET requests
    def get(self, request, hotel_id):
        hotel = get_object_or_404(Hotel, pk=hotel_id)  # Get the hotel object or return a 404 error
        form = ReviewForm()  # Instantiate an empty review form
        return render(request, 'bookings/add_review.html', {'form': form, 'hotel': hotel})  # Render the form and hotel in the template

    # Handle POST requests
    def post(self, request, hotel_id):
        hotel = get_object_or_404(Hotel, pk=hotel_id)  # Get the hotel object or return a 404 error
        form = ReviewForm(request.POST)  # Instantiate the form with POST data
        if form.is_valid():  # Check if the form is valid
            review = form.save(commit=False)  # Create a review object without saving to the database yet
            customer, created = Customer.objects.get_or_create(user=request.user)  # Get or create a customer object for the current user
            review.customer = customer  # Assign the customer to the review
            review.hotel = hotel  # Assign the hotel to the review
            review.save()  # Save the review to the database
            return redirect('hotel_detail', hotel_id=hotel.id)  # Redirect to the hotel detail page
        return render(request, 'bookings/add_review.html', {'form': form, 'hotel': hotel})  # Render the form and hotel in the template if form is invalid

# View for the home page
class HomeView(View):
    def get(self, request):
        return render(request, 'bookings/home.html')  # Render the home page template

# View for the hotel list
class HotelListView(View):
    def get(self, request):
        hotels = Hotel.objects.all()  # Get all hotel objects
        return render(request, 'bookings/hotel_list.html', {'hotels': hotels})  # Render the hotel list template with the hotels

# View for hotel details
class HotelDetailView(View):
    def get(self, request, hotel_id):
        hotel = get_object_or_404(Hotel, pk=hotel_id)  # Get the hotel object or return a 404 error
        rooms = Room.objects.filter(hotel=hotel)  # Get all rooms for the hotel
        reviews = Review.objects.filter(hotel=hotel)  # Get all reviews for the hotel
        return render(request, 'bookings/hotel_detail.html', {
            'hotel': hotel,
            'rooms': rooms,
            'reviews': reviews
        })  # Render the hotel detail template with the hotel, rooms, and reviews

# View for room details
class RoomDetailView(View):
    def get(self, request, room_id):
        room = get_object_or_404(Room, pk=room_id)  # Get the room object or return a 404 error
        return render(request, 'bookings/room_detail.html', {'room': room})  # Render the room detail template with the room

# View for the booking list
class BookingListView(View):
    def get(self, request):
        bookings = Booking.objects.select_related('customer', 'room').all()  # Get all bookings with related customer and room objects
        return render(request, 'bookings/booking_list.html', {'bookings': bookings})  # Render the booking list template with the bookings

# View for booking details
class BookingDetailView(View):
    def get(self, request, booking_id):
        booking = get_object_or_404(Booking, pk=booking_id)  # Get the booking object or return a 404 error
        return render(request, 'bookings/booking_detail.html', {'booking': booking})  # Render the booking detail template with the booking

# View for the review list
class ReviewListView(View):
    def get(self, request):
        reviews = Review.objects.all()  # Get all review objects
        return render(request, 'bookings/review_list.html', {'reviews': reviews})  # Render the review list template with the reviews
