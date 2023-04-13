from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, SellerProfile
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
        "id",
        "phone_number",
        "first_name",
    )
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        ("Permissions", {"fields": ("role", "is_staff", "is_active")}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "first_name",
                    "mid_name",
                    "last_name",
                    "dob",
                    "email",
                    "role",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    search_fields = ("phone_number",)
    ordering = ("phone_number", "first_name")
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(SellerProfile)
admin.site.unregister(Group)
