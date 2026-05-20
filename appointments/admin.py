from django.contrib import admin
from .models import AvailabilitySlot, Booking

'''admin.site.register(AvailabilitySlot)
admin.site.register(Booking)'''

@admin.register(AvailabilitySlot)
class AvailabilitySlotAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'doctor',
        'start_time',
        'end_time',
        'is_booked'
    )

admin.site.register(Booking)
