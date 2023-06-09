# Generated by Django 4.2 on 2023-04-12 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SellerProfile",
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
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profile_image",
                        verbose_name="Profile Picture",
                    ),
                ),
                (
                    "user_verification_document",
                    models.ImageField(
                        upload_to="user_verifcation",
                        verbose_name="User Verification Document",
                    ),
                ),
                (
                    "total_sales",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=6,
                        verbose_name="Seller Total Sales",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
