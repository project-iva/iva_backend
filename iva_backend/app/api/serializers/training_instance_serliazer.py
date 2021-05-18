from rest_framework import serializers
from iva_backend.app.models import TrainingInstance


class TrainingInstanceSerializer(serializers.ModelSerializer):
    intent_label = serializers.ReadOnlyField(source='intent.intent')

    class Meta:
        model = TrainingInstance
        fields = ['uuid', 'message_text', 'intent', 'created_at', 'intent_label', 'approved']
        read_only_fields = ['uuid', 'created_at']


class ExportTrainingInstancesSerializer(serializers.ModelSerializer):
    intent_label = serializers.ReadOnlyField(source='intent.intent')

    class Meta:
        model = TrainingInstance
        fields = ['message_text', 'intent_label']
