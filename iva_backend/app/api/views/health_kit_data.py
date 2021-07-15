from rest_framework import viewsets

from iva_backend.app.api.filter_backends import LimitFilterBackend
from iva_backend.app.api.serializers.health_kit_data import MindfulSessionSerializer, SleepAnalysisSerializer, \
    BodyMassSerializer
from iva_backend.app.models import MindfulSession, SleepAnalysis, BodyMass


class MindfulSessionsViewSet(viewsets.ModelViewSet):
    queryset = MindfulSession.objects.all()
    serializer_class = MindfulSessionSerializer
    filter_backends = [LimitFilterBackend]


class SleepAnalysesViewSet(viewsets.ModelViewSet):
    queryset = SleepAnalysis.objects.all()
    serializer_class = SleepAnalysisSerializer
    filter_backends = [LimitFilterBackend]


class BodyMassesViewSet(viewsets.ModelViewSet):
    queryset = BodyMass.objects.all()
    serializer_class = BodyMassSerializer
    filter_backends = [LimitFilterBackend]
