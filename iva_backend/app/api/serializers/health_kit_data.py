from rest_framework import serializers
from iva_backend.app.models import MindfulSession, SleepAnalysis, BodyMass


class MindfulSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MindfulSession
        exclude = ['created_at']


class ReadOnlyMindfulSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MindfulSession
        fields = ['start', 'end', 'duration_in_secs']
        read_only_fields = ['start', 'end', 'duration_in_secs']


class GroupedMindfulSessionSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    mindful_sessions = ReadOnlyMindfulSessionSerializer(many=True)


class SleepAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepAnalysis
        exclude = ['created_at']

class ReadOnlySleepAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepAnalysis
        fields = ['start', 'end', 'value', 'duration_in_secs']
        read_only_fields = ['start', 'end', 'value', 'duration_in_secs']

class GroupedSleepAnalysisSerializer(serializers.Serializer):
    date = serializers.DateField()
    sleep_analyses = ReadOnlySleepAnalysisSerializer(many=True)


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
