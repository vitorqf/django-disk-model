from django.db import models

# Create your models here.
class Disk(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    seal = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    gender = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name