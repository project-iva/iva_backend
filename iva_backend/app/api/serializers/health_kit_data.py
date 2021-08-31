from rest_framework import serializers
from iva_backend.app.models import MindfulSession, SleepAnalysis, BodyMass


class MindfulSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MindfulSession
        exclude = ['created_at']


class GroupedMindfulSessionSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    mindful_sessions = MindfulSessionSerializer(many=True)


class SleepAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepAnalysis
        exclude = ['created_at']


class GroupedSleepAnalysisSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    sleep_analyses = SleepAnalysisSerializer(many=True)


class BodyMassSerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField(source='recorded_at')

    class Meta:
        model = BodyMass
        fields = ['uuid', 'start', 'value']


class BodyMassStatsSerializer(serializers.Serializer):
    latest_measurement = serializers.FloatField()
    week_average = serializers.FloatField()
    prev_week_average = serializers.FloatField()
    month_average = serializers.FloatField()
    prev_month_average = serializers.FloatField()
