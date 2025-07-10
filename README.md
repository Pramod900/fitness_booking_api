## 🚀 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/fitness-booking-api.git
cd fitness-booking-api

# 2. Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Load seed data ******
python manage.py seed

# 6. Run the server
python manage.py runserver


For Postman requests
1️⃣ GET /api/classes/ – Fetch All Upcoming Classes
POST http://127.0.0.1:8000/api/classes/

[
    {
        "id": 7,
        "name": "Yoga",
        "instructor": "Alice",
        "start_time": "2025-07-10T18:33:27.424986+05:30",
        "available_slots": 10
    },
    {
        "id": 8,
        "name": "Zumba",
        "instructor": "Rahul",
        "start_time": "2025-07-10T18:33:27.424986+05:30",
        "available_slots": 8
    },
    {
        "id": 9,
        "name": "HIIT",
        "instructor": "Manoj Mehta",
        "start_time": "2025-07-10T18:33:27.440676+05:30",
        "available_slots": 6
    }
]

2️⃣ POST /api/book/ – Book a Fitness Class
POST http://127.0.0.1:8000/api/book/

{
    "class_id": 8,
    "client_name": "Pramod Jangir",
    "client_email": "pramod@gmail.com"
}

3️⃣ GET /api/bookings/?email=pramod@gmail.com – Get All Bookings by Email
GET http://127.0.0.1:8000/api/bookings/?email=pramod@gmail.com
[
    {
        "id": 10,
        "class_id": 8,
        "client_name": "Pramod Jangir",
        "client_email": "pramod@gmail.com",
        "booked_at": "2025-07-10T18:35:27.161002+05:30"
    }
]

