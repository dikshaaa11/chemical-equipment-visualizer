# Chemical Equipment Visualizer

A full-stack web application for analyzing chemical equipment datasets, visualizing distributions, and generating downloadable PDF summary reports.

This project was built as part of an internship / academic task to demonstrate full-stack development, authentication, data processing, and reporting.

---

## 🚀 Features

- JWT-based authentication (login required)
- Upload CSV files containing chemical equipment data
- Automatic data analysis:
  - Total equipment count
  - Average flowrate, pressure, temperature
  - Equipment type distribution
- Interactive bar chart visualization (Chart.js)
- Auto-generated PDF summary report (downloadable)
- Upload history tracking
- Clean API separation between frontend and backend

---

## 🧰 Tech Stack

### Frontend
- React (Vite)
- Chart.js
- Axios

### Backend
- Django
- Django REST Framework
- SimpleJWT (Authentication)
- ReportLab (PDF generation)

### Database
- SQLite (development)

---

## 📂 Required CSV Format

The uploaded CSV file **must contain the following columns**:

- `Equipment Name`
- `Type`
- `Flowrate`
- `Pressure`
- `Temperature`

---

## 🔐 Authentication Flow

1. User logs in via frontend
2. JWT access token is stored in browser
3. Token is sent in headers for:
   - CSV upload
   - PDF download
   - Upload history

Unauthorized requests are rejected by the backend.

---

## 📄 PDF Report

- Generated automatically after successful CSV upload
- Stored on the backend server
- Securely downloaded via authenticated API endpoint

---

## 🖥️ How to Run Locally

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
