# Mini Hospital Management System (HMS)

A backend-focused Hospital Management System built using Django, Django REST Framework, PostgreSQL, and a separate Python Serverless Email Service using the Serverless Framework.

The system supports doctor and patient workflows including appointment booking, slot management, serverless email notifications, and Google Calendar event simulation.

---

# Features

## Authentication
- Doctor signup and login
- Patient signup and login
- Token-based authentication
- Password hashing using Django authentication system
- Role-based access control

## Doctor Features
- Create availability slots
- View own slots
- Manage own bookings only

## Patient Features
- View available doctor slots
- Book appointments
- Prevent double booking

## Appointment System
- Slot blocking after booking
- Race condition handling using database locking
- Booking confirmation workflow

## Google Calendar Integration
- Simulated Google Calendar event creation
- Appointment event logs generated after booking

## Serverless Email Service
Separate Python serverless function using:
- Serverless Framework
- serverless-offline
- Gmail SMTP

Supported triggers:
- SIGNUP_WELCOME
- BOOKING_CONFIRMATION

---

# Tech Stack

## Backend
- Django
- Django REST Framework

## Database
- PostgreSQL

## Authentication
- DRF Token Authentication

## Serverless
- Serverless Framework
- serverless-offline

## Email
- Gmail SMTP

---

# Project Structure

```text
mini-hms/
│
├── README.md
├── requirements.txt
├── ai-tool-usage-log/
│
│── accounts/
|── appointments/
│── hms/
│── manage.py
│
└── email-service/
    ├── handler.py
    ├── serverless.yml
    └── package.json