# hotel_booking_system/urls.py (project-level)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookings.urls')),  # Include the app's urls.py here
]
