# Generated by Django 5.0.3 on 2024-04-06 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trekkings', '0009_booking'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='Book',
        ),
    ]
