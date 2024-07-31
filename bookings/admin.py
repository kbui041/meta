from django.contrib import admin
from django.utils.html import mark_safe
from .models import Customer, Hotel, Room, Booking, Review, Amenity, RoomImage, RoomAmenity, HotelCategory

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'image_preview')
    list_filter = ('city', 'country')
    search_fields = ('name', 'city', 'country')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image_url:
            return mark_safe(f'<img src="{obj.image_url}" width="100" height="100" />')
        return ""

    image_preview.short_description = 'Image Preview'

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Customer)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Amenity)
admin.site.register(RoomImage)
admin.site.register(RoomAmenity)
admin.site.register(HotelCategory)
