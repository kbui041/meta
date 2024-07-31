from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Define the URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # URL pattern for the Django admin site
    path('', include('bookings.urls')),  # Include the main app URLs for the 'bookings' app
    path('api/', include('bookings.urls_api')),  # Include the API URLs for the 'bookings' app
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)