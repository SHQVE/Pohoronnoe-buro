from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)

    login = models.EmailField(unique=True)
    password = models.CharField(max_length=31, null=False)
    bithdate = models.CharField(max_length=15, null=False)
    gender = models.CharField(max_length=2, null=False)
    confirm = models.BooleanField(default=False, null=False)
