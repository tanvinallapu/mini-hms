from rest_framework import serializers
from .models import AvailabilitySlot, Booking


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailabilitySlot
        fields = '__all__'
        read_only_fields = ['doctor', 'is_booked']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'