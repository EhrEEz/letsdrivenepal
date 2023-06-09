# Generated by Django 4.2 on 2023-04-12 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0002_sellerprofile"),
        ("vehicles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehicle",
            name="vehicle_image",
            field=models.ImageField(
                default="", upload_to="vehicle_image", verbose_name="Vehicle Image"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="vehicle",
            name="vehicle_owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="authentication.sellerprofile",
                verbose_name="Vehicle Owner",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="slug",
            field=models.TextField(
                blank=True, null=True, unique=True, verbose_name="Vehicle Slug"
            ),
        ),
        migrations.CreateModel(
            name="VehicleDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("modification_date", models.DateTimeField(auto_now=True)),
                (
                    "registration_document",
                    models.ImageField(
                        upload_to="vehicle_details",
                        verbose_name="Vehicle Bluebook Information",
                    ),
                ),
                (
                    "vehicle_verified",
                    models.BooleanField(
                        default=False, verbose_name="Vehicle Verification"
                    ),
                ),
                (
                    "vehicle_daily_price",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Cost of renting the Vehicle for a day",
                        max_digits=6,
                        verbose_name="Vehicle Price",
                    ),
                ),
                (
                    "vehicle_main",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicles.vehicle",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
