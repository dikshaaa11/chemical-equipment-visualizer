# Chemical Equipment Visualizer

A full-stack web application to upload CSV datasets of chemical equipment and visualize key statistics.

## Tech Stack
- Backend: Django REST Framework
- Frontend: React (Vite)
- Database: SQLite
- Charts: Recharts
- API Testing: Postman

## Features
- Upload CSV files
- Validate dataset columns
- Compute summary statistics
- Visualize equipment type distribution
- View upload history

## Required CSV Columns
- Equipment Name
- Type
- Flowrate
- Pressure
- Temperature

## How to Run Locally

### Backend
```bash
cd backend
venv\Scripts\activate
python manage.py runserver

## How to Run (Web)
1. Start backend
2. Start frontend

## How to Run (Desktop)
npm run electron