from rest_framework import serializers
from iva_backend.app.models import MindfulSession, SleepAnalysis


class MindfulSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MindfulSession
        exclude = ['created_at']


class SleepAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepAnalysis
        exclude = ['created_at']
