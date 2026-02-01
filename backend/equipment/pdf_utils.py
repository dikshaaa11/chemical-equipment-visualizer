from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from django.conf import settings
import os
import time

def generate_pdf(summary):
    filename = f"report_{int(time.time())}.pdf"
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica", 12)

    c.drawString(50, y, "Chemical Equipment Report")
    y -= 40

    c.drawString(50, y, f"Total Equipment: {summary['total_equipment']}")
    y -= 20
    c.drawString(50, y, f"Average Flowrate: {summary['avg_flowrate']}")
    y -= 20
    c.drawString(50, y, f"Average Pressure: {summary['avg_pressure']}")
    y -= 20
    c.drawString(50, y, f"Average Temperature: {summary['avg_temperature']}")

    y -= 30
    c.drawString(50, y, "Type Distribution:")
    y -= 20

    for k, v in summary["type_distribution"].items():
        c.drawString(70, y, f"{k}: {v}")
        y -= 18


    c.save()

    return filename
