# Generated by Django 5.0.3 on 2024-04-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trekkings', '0008_remove_register_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=50)),
                ('arrival_date', models.DateField()),
                ('leaving_date', models.DateField()),
                ('details', models.TextField()),
            ],
        ),
    ]