from django.db import models


# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.IntegerField()
    doors = models.IntegerField()
    grade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
