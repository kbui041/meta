from django.apps import AppConfig

# Configuration class for the 'bookings' app
class BookingsConfig(AppConfig):
    # Setting the default type for auto-generated primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    # Name of the app
    name = 'bookings'

    # This method is called when the app is ready to be used
    def ready(self):
        # Import signals to ensure they are registered when the app is loaded
        import bookings.signals
