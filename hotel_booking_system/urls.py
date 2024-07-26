from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookings.urls')),  # Main app URLs
    path('api/', include('bookings.urls_api')),  # API URLs
]
