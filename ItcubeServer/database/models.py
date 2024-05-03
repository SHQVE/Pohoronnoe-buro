from django.db import models
from django.conf import settings


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(null=False, max_length=255)
    date = models.DateField(null=False)
    checked = models.BooleanField(default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )

    date_implementation = models.DateField(null=True)
    implementer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name="task_implementer"
    )


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(null=False, max_length=63)
    company = models.CharField(null=False, max_length=63)
    body = models.CharField(null=False, max_length=31)
    type = models.CharField(null=False, max_length=63)
    weight = models.IntegerField(null=False, default=0)
    price = models.IntegerField(null=False, default=0)
    levy = models.FloatField(null=False, default=0.0)
    horse_power = models.IntegerField(null=False, default=0)
