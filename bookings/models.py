from django.db import models
from django.contrib.auth.models import User

class HotelCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, default='000-000-0000')

    def __str__(self):
        return self.user.username

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    category = models.ForeignKey(HotelCategory, on_delete=models.CASCADE)
    description = models.TextField(default='No description available')

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amenities = models.ManyToManyField('Amenity', through='RoomAmenity')

    def __str__(self):
        return f'{self.room_type} - {self.hotel.name}'

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f'Booking by {self.customer.user.username} for {self.room}'

class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.hotel.name}'

class Amenity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class RoomAmenity(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images/')
