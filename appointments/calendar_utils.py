import json
from datetime import datetime

def create_calendar_event(
    doctor_name,
    patient_name,
    start_time,
    end_time
):

    event = {
        "doctor": doctor_name,
        "patient": patient_name,
        "start": str(start_time),
        "end": str(end_time),
        "created_at": str(datetime.now())
    }

    print("GOOGLE CALENDAR EVENT CREATED")
    print(json.dumps(event, indent=4))

    with open("calendar_events.txt", "a") as file:
        file.write(json.dumps(event))
        file.write("\n")