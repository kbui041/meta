"""
ASGI config for hotel_booking_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Set the default Django settings module for the 'asgi' command
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_booking_system.settings')

# Get the ASGI application
application = get_asgi_application()
