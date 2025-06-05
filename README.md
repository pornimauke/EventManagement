# Mini Event Management System API (FastAPI)

## Overview

This is a **Mini Event Management System** built using **FastAPI** and **SQLAlchemy**, following clean architecture principles. The system allows users to:

- Create and list events
- Register attendees
- View attendee lists per event
- Handle edge cases like overbooking or duplicate registrations
- Timezone-aware event scheduling

## Project Structure

```
event_mgmt/
├── app/
│   ├── main.py                   # FastAPI app and routing setup
│   ├── db/database.py            # Database engine and Base setup
│   ├── models/
│   │   ├── event.py              # SQLAlchemy Event model
│   │   └── attendee.py           # SQLAlchemy Attendee model
│   ├── routes/event_routes.py    # API endpoints
│   ├── schemas/
│   │   ├── event.py              # Pydantic Event schemas
│   │   └── attendee.py           # Pydantic Attendee schemas
├── requirements.txt              # Dependencies
├── README.md                     # This file
```

## Started

### Prerequisites

- Python 3.8+
- VS Code (recommended)
- `virtualenv` installed (`pip install virtualenv`)

###  Setup Instructions

1. **Clone the repo or extract the zip:**

   ```bash
   cd D:\VS_CODE_Event_Mang
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate    # On Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**

   ```bash
   uvicorn app.main:app --reload
   ```

5. **Open in browser:**

   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) – Swagger UI
   - [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) – ReDoc UI

## API Endpoints

### POST `/events`

Create a new event.
```json
{
  "name": "Demo",
  "location": "Nagpur",
  "start_time": "2025-06-10T10:00:00",
  "end_time": "2025-06-10T12:00:00",
  "max_capacity": 10
}
```

### GET `/events`

List all **upcoming events**.

### POST `/events/{event_id}/register`

Register an attendee with:
```json
{
  "name": "Pornima",
  "email": "pornimauke22@gmail.com"
}
```

## Validations:
- Prevents overbooking (max capacity)
- Prevents duplicate registration (email-based)

### GET `/events/{event_id}/attendees`

Returns a list of all registered attendees for the event.

## Features

- FastAPI for modern async web framework
- SQLite + SQLAlchemy for ORM
- Swagger UI for auto API documentation
- Validation using Pydantic
- Clean modular architecture
- Timezone support (IST to other zones)
- Ready for unit testing with `pytest`
- Pagination support (extendable)

## Dependencies

fastapi
uvicorn
sqlalchemy
pydantic

Install using:

```bash
pip install -r requirements.txt
```
