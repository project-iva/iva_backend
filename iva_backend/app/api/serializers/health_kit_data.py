from rest_framework import serializers
from iva_backend.app.models import MindfulSession, SleepAnalysis, BodyMass


class MindfulSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MindfulSession
        exclude = ['created_at']


class SleepAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepAnalysis
        exclude = ['created_at']


class BodyMassSerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField(source='recorded_at')

    class Meta:
        model = BodyMass
        fields = ['uuid', 'start', 'value']
