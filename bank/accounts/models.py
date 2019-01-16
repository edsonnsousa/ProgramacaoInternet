from django.db import models


# Create your models here.
class Account(models.Model):
    owner = models.CharField(max_length=30),
    balance = models.DecimalField(max_digits = 20, decimal_places = 2),
    creation_date = models.DateField()


class Meta:
    ordering = ('owner',)

