from rest_framework import serializers
from iva_backend.app.models.mindful_session import MindfulSession
from datetime import datetime
from django.utils.timezone import make_aware


class MindfulSessionSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        # convert start and end from unix timestamp to datetime
        start = data.get('start')
        if (start is not None) and isinstance(start, float):
            data['start'] = make_aware(datetime.fromtimestamp(start))

        end = data.get('end')
        if (end is not None) and isinstance(end, float):
            data['end'] = make_aware(datetime.fromtimestamp(end))
        return super().to_internal_value(data)

    class Meta:
        model = MindfulSession
        fields = '__all__'
