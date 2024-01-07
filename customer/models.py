from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=11)
    address = models.TextField(max_length=400)
    birth_date = models.DateField()
    age = models.PositiveIntegerField()

    class Meta:
        verbose_name = "customer"
        verbose_name_plural = "customers"

        pass
