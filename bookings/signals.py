from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Customer

# Signal receiver function to create a Customer instance when a new User is created
@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

# Signal receiver function to save the Customer instance when the User is saved
@receiver(post_save, sender=User)
def save_customer(sender, instance, **kwargs):
    instance.customer.save()
