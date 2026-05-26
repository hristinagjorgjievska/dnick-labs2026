from django.contrib import admin

from .models import Instructor, Category, Training

# Register your models here.
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ["name", "biography", "experience_level"]
    exclude = ["surname"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "is_popular"]

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ["name", "instructor", "category", "user", "price", "free_spots"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)