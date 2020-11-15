from rest_framework import serializers
from iva_backend.app.models import Intent, TrainingInstance


class IntentSerializer(serializers.ModelSerializer):
    training_instances_count = serializers.SerializerMethodField()

    def get_training_instances_count(self, obj):
        return obj.training_instances.count()

    class Meta:
        model = Intent
        fields = '__all__'


class TrainingInstanceSerializer(serializers.ModelSerializer):
    intent_label = serializers.ReadOnlyField(source='intent.intent')

    class Meta:
        model = TrainingInstance
        fields = ['uuid', 'message_text', 'intent', 'created_at', 'intent_label']
