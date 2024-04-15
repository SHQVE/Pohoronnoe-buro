from django.db import models
from django.conf import settings


class User(models.Model):
    id = models.AutoField(primary_key=True)

    login = models.EmailField(unique=True)
    password = models.CharField(max_length=31, null=False)
    bithdate = models.CharField(max_length=15, null=False)
    gender = models.CharField(max_length=2, null=False)
    confirm = models.BooleanField(default=False, null=False)


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
