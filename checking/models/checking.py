from django.db import models


class CheckingDuration(models.Model):
    name = models.CharField(max_length=255)
    hours = models.PositiveIntegerField()
    time_from = models.DateTimeField()
    time_to = models.DateTimeField()

    def __str__(self):
        return self.name


from reservation.models.reservation import Reservation
from customer.models import Customer
from room.models.room import Room

CHECKING_CHOICES = [
    ("walk_in", "Walk-In"),
    ("with_reservation", "With Reservation"),
]


class Checking(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    checking_type = models.CharField(max_length=20, choices=CHECKING_CHOICES)

    def check_in(self):
        pass

    def check_out(self):
        pass

    def check_term(self):
        pass

    def check_extend(self):
        pass

    def make_payment(self):
        pass


TERM_CHOICES = [
    ("check_in", "Checked In"),
    ("check_out", "Checked Out"),
]


class CheckingTerm(models.Model):
    checking = models.ForeignKey("Checking", on_delete=models.PROTECT)
    checking_duration = models.ForeignKey("CheckingDuration", on_delete=models.PROTECT)
    state = models.CharField(max_length=20, choices=TERM_CHOICES)
    active = models.BooleanField(default=False)

    def get_state(self):
        self.state

    @property
    def is_checked_in(self):
        return self.state == "check_in"

    @property
    def is_checked_out(self):
        return self.state == "check_out"
