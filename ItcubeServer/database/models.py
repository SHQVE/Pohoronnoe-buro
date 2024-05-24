from django.db import models
from django.conf import settings


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(null=False, max_length=63)
    brand = models.CharField(null=False, max_length=63)
    body = models.CharField(null=False, max_length=31)
    type = models.CharField(null=False, max_length=63)
    weight = models.IntegerField(null=False, default=0)
    price = models.IntegerField(null=False, default=0)
    levy = models.FloatField(null=False, default=0.0)
    horse_power = models.IntegerField(null=False, default=0)
    color = models.CharField(null=False, max_length=31)

    date = models.DateField(null=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
