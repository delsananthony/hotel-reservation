from django.db import models


# Create your models here.
class RoomCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    active = models.BooleanField(default=False)

    @property
    def is_active(self):
        return self.active

    class Meta:
        verbose_name = "room_category"
        verbose_name_plural = "room_categories"
        ordering = [
            "name",
        ]
