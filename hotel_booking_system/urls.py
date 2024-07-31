from django.contrib import admin
from django.urls import path, include

# Define the URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # URL pattern for the Django admin site
    path('', include('bookings.urls')),  # Include the main app URLs for the 'bookings' app
    path('api/', include('bookings.urls_api')),  # Include the API URLs for the 'bookings' app
]
