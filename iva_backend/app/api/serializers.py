from rest_framework import serializers
from iva_backend.app.models import Intent, TrainingInstance


class IntentSerializer(serializers.ModelSerializer):
    training_instances_count = serializers.SerializerMethodField()

    def get_training_instances_count(self, obj):
        return obj.training_instances.filter(approved=True).count()

    class Meta:
        model = Intent
        fields = '__all__'


class TrainingInstanceSerializer(serializers.ModelSerializer):
    intent_label = serializers.ReadOnlyField(source='intent.intent')

    class Meta:
        model = TrainingInstance
        fields = ['uuid', 'message_text', 'intent', 'created_at', 'intent_label', 'approved']


class ExportTrainingInstancesSerializer(serializers.ModelSerializer):
    intent_label = serializers.ReadOnlyField(source='intent.intent')

    class Meta:
        model = TrainingInstance
        fields = ['message_text', 'intent_label']
