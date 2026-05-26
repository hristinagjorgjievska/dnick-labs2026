from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Cuisine(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    is_trending = models.BooleanField()

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    max_capacity = models.PositiveIntegerField()

class Reservation(models.Model):
    STATUS = [
        ("AP", "APPROVED"),
        ("PE", "PENDING"),
        ("RE", "REJECTED")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    num_of_guests = models.PositiveIntegerField(default=0)
    extra_requests = models.TextField(blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS)
    estimated_price = models.PositiveIntegerField()
