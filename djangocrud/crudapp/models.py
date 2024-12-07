from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100, verbose_name="Car Name")
    brand = models.CharField(max_length=100, verbose_name="Car Brand")
    model = models.CharField(max_length=100, verbose_name="Car Model")
    price = models.IntegerField(verbose_name="Car Price")

    def __str__(self):
        return str(self.id)