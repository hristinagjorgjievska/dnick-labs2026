from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Lecturer)
class Lecturer(admin.ModelAdmin):
    list_display = ["name", "surname", "experience_level"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "is_popular"]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "lecturer", "category", "user", "price", "free_spots"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

