from django.db import models


class Makes(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Autos(models.Model):

    nickname = models.CharField(max_length=100)
    make = models.ForeignKey(Makes, on_delete=models.CASCADE)
    mileage = models.IntegerField()
    comments = models.CharField(max_length=256)
