from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Company(models.Model):
    TYPE = [
        ("S", "SMALL"),
        ("M", "MEDIUM"),
        ("L", "LARGE")
    ]

    name = models.CharField(max_length=20)
    date = models.DateField()
    type = models.CharField(choices=TYPE)


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    is_active = models.BooleanField()

class Supplement(models.Model):
    name = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()



