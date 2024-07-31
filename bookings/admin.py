from django.contrib import admin
from .models import Customer, Hotel, Room, Booking, Review, Amenity, RoomImage, RoomAmenity, HotelCategory

# Register the Customer model with the admin site
admin.site.register(Customer)

# Register the Hotel model with the admin site
admin.site.register(Hotel)

# Register the Room model with the admin site
admin.site.register(Room)

# Register the Booking model with the admin site
admin.site.register(Booking)

# Register the Review model with the admin site
admin.site.register(Review)

# Register the Amenity model with the admin site
admin.site.register(Amenity)

# Register the RoomImage model with the admin site
admin.site.register(RoomImage)

# Register the RoomAmenity model with the admin site
admin.site.register(RoomAmenity)

# Register the HotelCategory model with the admin site
admin.site.register(HotelCategory)
