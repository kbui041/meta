# Generated by Django 5.0.7 on 2024-07-24 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_remove_review_user_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='phone_number',
            field=models.CharField(default='000-000-0000', max_length=20),
        ),
    ]
