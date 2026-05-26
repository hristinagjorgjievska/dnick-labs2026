from django.contrib import admin

from .models import Cuisine, Restaurant, Reservation


# Register your models here.
@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ["name", "country", "description", "is_trending"]


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "cuisine", "max_capacity"]

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["user", "date", "num_of_guests", "restaurant", "status", "estimated_price"]
    list_filter = ["status"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)
