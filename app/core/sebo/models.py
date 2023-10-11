from django.db import models

# Create your models here.
class Disk(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    seal = models.ForeignKey('Seal', on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    gender = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    artists = models.ManyToManyField('Artist')

    def __str__(self) -> str:
        return self.name
    
class Seal(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
    
class Artist(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name