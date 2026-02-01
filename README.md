# Chemical Equipment Visualizer

A full-stack web application to upload CSV datasets of chemical equipment, analyze key statistics, visualize equipment distributions, and generate secure PDF summary reports.

---

##  Overview

This project allows users to:
- Log in securely using JWT authentication
- Upload CSV files containing chemical equipment data
- View computed summary statistics
- Visualize equipment type distribution using charts
- Download an auto-generated PDF report
- Track upload history

---

##  Tech Stack

### Frontend
- React
- Vite
- Chart.js
- Axios

### Backend
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- Pandas (CSV processing)
- ReportLab (PDF generation)

### Database
- SQLite (default, for development)

---

##  Features

-  JWT-based authentication
-  CSV upload with validation
-  Automatic data analysis:
  - Total equipment count
  - Average flowrate
  - Average pressure
  - Average temperature
  - Equipment type distribution
-  Interactive bar chart visualization
-  Secure PDF report generation and download
-  Upload history tracking
-  No large files or binaries committed to GitHub

---

##  Required CSV Columns

Your CSV file **must** contain the following columns:

Equipment Name
Type
Flowrate
Pressure
Temperature


---

##  How to Run Locally

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```
Backend runs at:

http://127.0.0.1:8000

Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

http://localhost:5173

 Authentication

Login uses JWT (/api/token/)

Access token is stored in browser localStorage

Protected endpoints:

CSV upload

Upload history

PDF download

PDF Reports

PDF reports are generated automatically after a successful CSV upload

Reports are stored temporarily on the backend

Users can securely download the report after authentication

Media files are not committed to GitHub

Git & Repository Notes:

node_modules/, media files, and binaries are excluded via .gitignore

No files larger than GitHub’s size limits are tracked

Repository contains only clean source code and sample data

Sample Data:

A sample CSV file is included:

sample_data/sample_equipment_data.csv


Use this to test uploads immediately after setup.
Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
No file chosen
Attach files by dragging & dropping, selecting or pasting them.
