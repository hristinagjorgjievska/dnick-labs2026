from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "date", "type"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "is_active"]

@admin.register(Supplement)
class SupplementAdmin(admin.ModelAdmin):
    list_display = ["name", "company", "category", "user", "price", "quantity"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)