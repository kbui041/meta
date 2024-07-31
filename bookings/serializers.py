from rest_framework import serializers
from .models import Hotel, Room, Booking, Review, Customer

# Serializer for the Hotel model
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model to serialize
        model = Hotel
        # Include all fields in the serialization
        fields = '__all__'

# Serializer for the Room model
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model to serialize
        model = Room
        # Include all fields in the serialization
        fields = '__all__'

# Serializer for the Booking model
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model to serialize
        model = Booking
        # Include all fields in the serialization
        fields = '__all__'

# Serializer for the Review model
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model to serialize
        model = Review
        # Include all fields in the serialization
        fields = '__all__'

# Serializer for the Customer model
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model to serialize
        model = Customer
        # Include all fields in the serialization
        fields = '__all__'
