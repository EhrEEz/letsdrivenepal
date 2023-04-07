from django.db import models
from django.utils.text import slugify


# Create your models here.
class BaseModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Vehicle(BaseModel):
    name = models.CharField("Vehicle Name", max_length=100)
    reg_no = models.CharField("Vehicle Registration Number", max_length=20)
    on_trip = models.BooleanField(
        "Vehicle is on trip", default=False, null=False, blank=False
    )
    seats = models.IntegerField("Vehicle Seat Limit")
    color_name = models.CharField("Vehicle Color Name", max_length=50)
    color_code = models.CharField("Vehicle Color Code", max_length=6)
    model_name = models.CharField("Vehicle Model Name", max_length=100)
    model_manufacturer = models.CharField("Vehicle Model Manufacturer", max_length=100)
    is_active = models.BooleanField(
        "Vehicle is active", default=True, null=False, blank=False
    )
    slug = models.TextField("Vehicle Slug", unique=True, null=True, blank=True)

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
        *args,
        **kwargs,
    ):
        self.is_active = True
        if self.color_name is None or self.color_name is "":
            self.color_name = self.color_code
        if self.slug is None or self.slug is "":
            self.slug = slugify(f"{self.name}-{self.reg_no}")
        if update_fields is not None and (
            "reg_no" in update_fields or "name" in update_fields
        ):
            update_fields = {"slug"}.union(update_fields)

        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
            *args,
            **kwargs,
        )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-modification_date", "-creation_date", "name"]
        verbose_name_plural = "Vehicles"
