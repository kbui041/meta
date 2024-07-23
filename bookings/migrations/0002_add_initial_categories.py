from django.db import migrations

def add_initial_categories(apps, schema_editor):
    Category = apps.get_model('bookings', 'Category')
    Category.objects.create(name='Luxury')
    Category.objects.create(name='Budget')
    Category.objects.create(name='Family')
    Category.objects.create(name='Business')
    Category.objects.create(name='Boutique')

class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_categories),
    ]
