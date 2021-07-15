from rest_framework import serializers
from iva_backend.app.models.intent import Intent


class IntentSerializer(serializers.ModelSerializer):
    training_instances_count = serializers.SerializerMethodField()

    def get_training_instances_count(self, obj):
        return obj.training_instances.filter(approved=True).count()

    class Meta:
        model = Intent
        fields = '__all__'
        read_only_fields = ['uuid']
