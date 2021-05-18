from rest_framework import viewsets

from iva_backend.app.api.serializers.health_kit_data_serializer import MindfulSessionSerializer
from iva_backend.app.models import MindfulSession


class MindfulSessionsViewSet(viewsets.ModelViewSet):
    queryset = MindfulSession.objects.all()
    serializer_class = MindfulSessionSerializer
