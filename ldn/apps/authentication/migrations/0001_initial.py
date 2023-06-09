# Generated by Django 4.2 on 2023-04-07 06:11

import apps.authentication.managers
import apps.authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        max_length=10,
                        unique=True,
                        validators=[apps.authentication.models.phone_validator],
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=64, verbose_name="First Name"),
                ),
                (
                    "mid_name",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="Middle Name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(max_length=64, verbose_name="Last Name"),
                ),
                ("dob", models.DateField()),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        unique=True,
                        verbose_name="Email",
                    ),
                ),
                (
                    "role",
                    models.IntegerField(
                        choices=[(1, "customer"), (2, "seller"), (0, "admin")]
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(auto_now_add=True, verbose_name="Date Joined"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="Staff Status",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
            managers=[
                ("objects", apps.authentication.managers.AccountManager()),
            ],
        ),
    ]
