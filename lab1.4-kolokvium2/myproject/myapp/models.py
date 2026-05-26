from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Lecturer(models.Model):
    EXPERIENCE_LEVEL = [
        ("BEG", "BEGINNER"),
        ("EX", "EXPERIENCED"),
        ("EXP", "EXPERT")
    ]

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    experience_level = models.CharField(choices=EXPERIENCE_LEVEL, max_length=20)


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=20)
    is_popular = models.BooleanField()

class Course(models.Model):
    name = models.CharField(max_length=20)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    description = models.TextField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    free_spots = models.PositiveIntegerField(default=0)

