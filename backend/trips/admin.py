from django.contrib import admin

from .models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "pick_up_address",
        "drop_off_address",
        "status",
        "created",
        "updated",
    )
    list_display = (
        "id",
        "pick_up_address",
        "drop_off_address",
        "status",
        "created",
        "updated",
    )
    list_filter = ("status",)
    readonly_fields = (
        "id",
        "created",
        "updated",
    )
