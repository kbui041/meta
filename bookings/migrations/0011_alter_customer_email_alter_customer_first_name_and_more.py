# Generated by Django 5.0.7 on 2024-08-01 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0010_room_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]