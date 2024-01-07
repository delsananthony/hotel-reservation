from django.contrib import admin


from room.models.room import Room
from room.models.room_category import RoomCategory

# Register your models here.
admin.site.register(Room)
admin.site.register(RoomCategory)
