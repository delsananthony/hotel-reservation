from django.db import models


from customer.models import Customer
from room.models.room import Room


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    date_reserved = models.DateTimeField()
    note = models.TextField(max_length=1000)

    def get_object_reservation(self):
        return self

    def __str__(self):
        return f"{self.room.name} - {self.customer.name}"

    class Meta:
        verbose_name = "reservation"
        verbose_name_plural = "reservations"
