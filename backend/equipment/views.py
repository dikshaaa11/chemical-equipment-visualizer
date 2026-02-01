import pandas as pd

from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    CSVUploadSerializer,
    DatasetSummarySerializer,
    UploadHistorySerializer,
)
from .models import UploadHistory
from .pdf_utils import generate_pdf


REQUIRED_COLUMNS = [
    "Equipment Name",
    "Type",
    "Flowrate",
    "Pressure",
    "Temperature",
]


@api_view(["GET"])
def test_api(request):
    return Response({"message": "API working successfully"})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def upload_csv(request):
    serializer = CSVUploadSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    file = serializer.validated_data["file"]

    if not file.name.endswith(".csv"):
        return Response(
            {"error": "Only CSV files are allowed"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        df = pd.read_csv(file)

        missing_columns = [c for c in REQUIRED_COLUMNS if c not in df.columns]
        if missing_columns:
            return Response(
                {
                    "error": "Missing required columns",
                    "missing_columns": missing_columns,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        summary_data = {
            "total_equipment": len(df),
            "avg_flowrate": round(float(df["Flowrate"].mean()), 2),
            "avg_pressure": round(float(df["Pressure"].mean()), 2),
            "avg_temperature": round(float(df["Temperature"].mean()), 2),
            "type_distribution": df["Type"].value_counts().to_dict(),
        }

        # ✅ Generate PDF AFTER summary exists
        pdf_path = generate_pdf(summary_data)
        summary_data["pdf_report"] = pdf_path

        # ✅ Save upload history
        UploadHistory.objects.create(
            total_equipment=summary_data["total_equipment"],
            avg_flowrate=summary_data["avg_flowrate"],
            avg_pressure=summary_data["avg_pressure"],
            avg_temperature=summary_data["avg_temperature"],
        )

        serializer = DatasetSummarySerializer(summary_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def upload_history(request):
    qs = UploadHistory.objects.all().order_by("-uploaded_at")
    serializer = UploadHistorySerializer(qs, many=True)
    return Response(serializer.data)


from django.http import FileResponse, Http404
from django.conf import settings
import os



from django.http import FileResponse, Http404
from django.conf import settings
from pathlib import Path

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def download_pdf(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    if not os.path.exists(file_path):
        raise Http404("PDF not found")

    return FileResponse(
        open(file_path, "rb"),
        content_type="application/pdf",
        as_attachment=True,
        filename=filename
    )


