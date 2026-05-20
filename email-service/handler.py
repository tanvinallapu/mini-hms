import json
import smtplib

from email.mime.text import MIMEText


SMTP_EMAIL = "xyzx58305@gmail.com"
SMTP_PASSWORD = "rjisjjbcltlmrnhd"


def send_email(event, context):
    body = json.loads(event.get("body", "{}"))

    email_type = body.get("type")
    receiver = body.get("email")
    username = body.get("username")

    if email_type == "SIGNUP_WELCOME":
        subject = "Welcome to HMS"
        message = f"Hello {username}, welcome to HMS platform."

    elif email_type == "BOOKING_CONFIRMATION":
        subject = "Booking Confirmation"
        message = "Your appointment has been booked successfully."

    else:
        subject = "HMS Notification"
        message = "Notification"

    msg = MIMEText(message)

    msg["Subject"] = subject
    msg["From"] = SMTP_EMAIL
    msg["To"] = receiver

    server = smtplib.SMTP("smtp.gmail.com", 587,timeout=10)

    server.starttls()

    server.login(SMTP_EMAIL, SMTP_PASSWORD)

    server.sendmail(
        SMTP_EMAIL,
        receiver,
        msg.as_string()
    )

    server.quit()
    print("FUNCTION EXECUTED")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "Email sent successfully"
        })
    }