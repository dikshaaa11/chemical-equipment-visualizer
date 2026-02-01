from rest_framework import serializers
from .models import UploadHistory


class CSVUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class DatasetSummarySerializer(serializers.Serializer):
    total_equipment = serializers.IntegerField()
    avg_flowrate = serializers.FloatField()
    avg_pressure = serializers.FloatField()
    avg_temperature = serializers.FloatField()
    type_distribution = serializers.DictField()
    pdf_report = serializers.CharField()   




class UploadHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadHistory
        fields = "__all__"
