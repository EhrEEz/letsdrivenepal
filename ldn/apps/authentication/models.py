from __future__ import unicode_literals
from django.db import models
from .managers import AccountManager
from django.core.exceptions import ValidationError
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail


def phone_validator(value):
    if len(value) != 10 or value.isdigit() is False:
        raise ValidationError(
            ("Please Enter a valid phone number"),
            params={"value": value},
        )


class User(AbstractBaseUser, PermissionsMixin):
    CUSTOMER = 1
    SELLER = 2
    ADMIN = 0

    ROLE_CHOICES = [
        (CUSTOMER, "customer"),
        (SELLER, "seller"),
        (ADMIN, "admin"),
    ]
    phone_number = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        unique=True,
        verbose_name="Phone Number",
        validators=[
            phone_validator,
        ],
    )
    first_name = models.CharField(max_length=64, verbose_name="First Name")
    mid_name = models.CharField(
        max_length=64, blank=True, null=True, verbose_name="Middle Name"
    )
    last_name = models.CharField(max_length=64, verbose_name="Last Name")
    dob = models.DateField(null=False, blank=False)
    email = models.EmailField(null=True, blank=True, verbose_name="Email", unique=True)
    role = models.IntegerField(choices=ROLE_CHOICES)
    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name="Date Joined", editable=False
    )
    is_active = models.BooleanField(default=True, verbose_name="Active")
    is_staff = models.BooleanField(
        verbose_name="Staff Status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    objects = AccountManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name", "dob", "role"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    @property
    def get_full_name(self):
        # Returns Full Name of the user
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def short_name(self):
        return self.first_name

    def __str__(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class SellerProfile(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    profile_image = models.ImageField(
        "Profile Picture", upload_to="profile_image", null=True, blank=True
    )
    user_verification_document = models.ImageField(
        "User Verification Document",
        upload_to="user_verifcation",
        null=False,
        blank=False,
    )
    total_sales = models.DecimalField(
        "Seller Total Sales", max_digits=6, decimal_places=2
    )
