import datetime

from django.db import models


class SmartShop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    year = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def age_shop(self):
        return datetime.datetime.now().year - self.year

class Iphone(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    harakter = models.TextField()
    smart_shop = models.ForeignKey(SmartShop, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name



