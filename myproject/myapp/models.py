from django.db import models

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    years_experience = models.PositiveIntegerField(default=0)
    website = models.URLField(null=True, blank=True)


class Training(models.Model):
    CATEGORY = [
        ("CARD", "CARDIO"),
        ("RES", "RESISTANCE"),
        ("YO", "YOGA"),
        ("HI", "HIIT"),
        ("PIL", "PILATES"),
        ("CROSS", "CROSS-FIT"),
        ("STR", "STRETCHING")
    ]

    LEVEL = [
        ("BEG", "BEGINNER"),
        ("INT", "INTERMEDIATE"),
        ("ADV", "ADVANCED")
    ]

    name = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY)
    level = models.CharField(max_length=20, choices=LEVEL)
    duration = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()


