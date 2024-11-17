# Flask Health System App

## Description
This is a Flask-based web application to manage health-related data, including users, patients, diseases, and other entities.
The app uses a PostgreSQL database hosted on Railway and is deployed as a public web service also on Railway.

## Features
- Add, view, edit, and delete records for various entities such as users, diseases, patients, and more.
- A relational database structure connecting multiple tables.
- Hosted and publicly accessible via Railway.

## Setup Instructions
1. Clone the repository:
git clone https://github.com/nurkhannury/flask_health_system.git cd flask_health_system

2. Set up a virtual environment:
python -m venv venv source venv/bin/activate # On Windows, use venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the app locally:
python app.py

6. Access the app at `http://127.0.0.1:5000`.
