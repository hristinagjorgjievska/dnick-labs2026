from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ["name", "country", "city", "years_experience"]

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ["name", "trainer", "category", "level", "duration", "capacity", "price"]
