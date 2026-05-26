from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Instructor(models.Model):
    EXPERIENCE = [
        ("BEG", "BEGINNER"),
        ("CERT", "CERTIFIED"),
        ("PROF", "PROFESSIONAL")
    ]

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    biography = models.TextField(null=True, blank=True)
    experience_level = models.CharField(choices=EXPERIENCE)


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    is_popular = models.BooleanField()

class Training(models.Model):
    name = models.CharField(max_length=20)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    price = models.PositiveIntegerField()
    free_spots = models.PositiveIntegerField()

