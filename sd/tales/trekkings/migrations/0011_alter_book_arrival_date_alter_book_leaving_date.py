# Generated by Django 5.0.3 on 2024-04-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trekkings', '0010_rename_booking_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='arrival_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='leaving_date',
            field=models.DateField(null=True),
        ),
    ]
