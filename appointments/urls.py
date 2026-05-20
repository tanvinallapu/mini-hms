from django.urls import path
from .views import (
    CreateAvailabilityView,
    AvailableSlotsView,
    BookAppointmentView
)

urlpatterns = [
    path(
        'create-slot/',
        CreateAvailabilityView.as_view()
    ),

    path(
        'available-slots/',
        AvailableSlotsView.as_view()
    ),

    path(
        'book/<int:slot_id>/',
        BookAppointmentView.as_view()
    ),
]