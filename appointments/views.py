import requests
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now

from .models import AvailabilitySlot
from .serializers import AvailabilitySerializer
from accounts.permissions import IsDoctor

from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Booking
from accounts.permissions import IsPatient

from .calendar_utils import create_calendar_event

class CreateAvailabilityView(generics.ListCreateAPIView):
    serializer_class = AvailabilitySerializer
    permission_classes = [IsAuthenticated, IsDoctor]

    def get_queryset(self):
        return AvailabilitySlot.objects.filter(
            doctor=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(doctor=self.request.user)


class AvailableSlotsView(generics.ListAPIView):
    serializer_class = AvailabilitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AvailabilitySlot.objects.filter(
            is_booked=False,
            start_time__gt=now()
        )

class BookAppointmentView(APIView):

    permission_classes = [IsAuthenticated, IsPatient]

    @transaction.atomic
    def post(self, request, slot_id):

        try:

            slot = AvailabilitySlot.objects.select_for_update().get(
                id=slot_id
            )

            if slot.is_booked:

                return Response(
                    {'message': 'Slot already booked'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            slot.is_booked = True
            slot.save()

            booking = Booking.objects.create(
                patient=request.user,
                doctor=slot.doctor,
                slot=slot
            )

            # Google Calendar Integration
            create_calendar_event(
                slot.doctor.username,
                request.user.username,
                slot.start_time,
                slot.end_time
            )

            # Booking Confirmation Email
            try:

                requests.post(
                    "http://localhost:3000/dev/send-email",
                    json={
                        "type": "BOOKING_CONFIRMATION",
                        "email": request.user.email,
                        "username": request.user.username
                    },
                    timeout=10
                )

                print("BOOKING EMAIL TRIGGERED")

            except Exception as e:

                print("BOOKING EMAIL ERROR")
                print(e)

            return Response({
                'message': 'Appointment booked successfully',
                'booking_id': booking.id
            })

        except AvailabilitySlot.DoesNotExist:

            return Response(
                {'message': 'Slot not found'},
                status=status.HTTP_404_NOT_FOUND
            )