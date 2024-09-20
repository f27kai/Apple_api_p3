from django.db import models

class Iphone(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    harakter = models.TextField()

    def __str__(self):
        return self.name

