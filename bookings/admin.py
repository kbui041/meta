from django.contrib import admin
from .models import Customer, Hotel, Room, Booking, Review, Amenity, RoomImage, RoomAmenity, HotelCategory

admin.site.register(Customer)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Amenity)
admin.site.register(RoomImage)
admin.site.register(RoomAmenity)
admin.site.register(HotelCategory)
