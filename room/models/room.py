from django.db import models


ROOM_CHOICES = [
    ("occupied", "Occupied"),
    ("vacant", "Vacant"),
    ("maintain", "Maintenance"),
]


class Room(models.Model):
    room_categ = models.ForeignKey("RoomCategory", on_delete=models.PROTECT)
    state = models.CharField(max_length=20, choices=ROOM_CHOICES)
    package_rate = models.PositiveIntegerField()
    hourly_rate = models.PositiveIntegerField()
    active = models.BooleanField(default=False)

    @property
    def is_active(self):
        return self.active

    class Meta:
        verbose_name = "room"
        verbose_name_plural = "rooms"
