# Generated by Django 5.0.7 on 2024-07-23 09:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_remove_room_amenities_customer_address_hotel_city_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='description',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_type',
        ),
        migrations.AddField(
            model_name='review',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bookings.customer'),
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='Default Room Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='amenity',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='booking',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='state',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hotelcategory',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
