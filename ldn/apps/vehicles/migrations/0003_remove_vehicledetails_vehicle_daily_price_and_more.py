# Generated by Django 4.2 on 2023-04-12 07:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vehicles", "0002_vehicle_vehicle_image_vehicle_vehicle_owner_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vehicledetails",
            name="vehicle_daily_price",
        ),
        migrations.AddField(
            model_name="vehicle",
            name="vehicle_daily_price",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                help_text="Cost of renting the Vehicle for a day",
                max_digits=6,
                verbose_name="Vehicle Price",
            ),
            preserve_default=False,
        ),
    ]