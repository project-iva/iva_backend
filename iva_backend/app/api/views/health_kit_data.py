from itertools import groupby

from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from iva_backend.app.api.filter_backends import LimitFilterBackend
from iva_backend.app.api.serializers.health_kit_data import MindfulSessionSerializer, SleepAnalysisSerializer, \
    BodyMassSerializer, GroupedSleepAnalysisSerializer, GroupedMindfulSessionSerializer
from iva_backend.app.models import MindfulSession, SleepAnalysis, BodyMass


class MindfulSessionsViewSet(viewsets.ModelViewSet):
    queryset = MindfulSession.objects.all()
    serializer_class = MindfulSessionSerializer
    filter_backends = [LimitFilterBackend]


class GroupedMindfulSessionsView(APIView):
    def get(self, request) -> Response:
        queryset = MindfulSession.objects.order_by('-end')
        result = [{'date': key, 'mindful_sessions': list(group)} for key, group in
                  groupby(queryset,
                          key=lambda mindful_session: timezone.localtime(mindful_session.end).strftime("%Y-%m-%d"))]
        serializer = GroupedMindfulSessionSerializer(data=result, many=True)
        serializer.is_valid()
        return Response(serializer.data)


class SleepAnalysesViewSet(viewsets.ModelViewSet):
    queryset = SleepAnalysis.objects.all()
    serializer_class = SleepAnalysisSerializer
    filter_backends = [LimitFilterBackend]


class GroupedSleepAnalysesView(APIView):
    def get(self, request) -> Response:
        queryset = SleepAnalysis.objects.order_by('-end')
        result = [{'date': key, 'sleep_analyses': list(group)} for key, group in
                  groupby(queryset,
                          key=lambda sleep_analysis: timezone.localtime(sleep_analysis.end).strftime("%Y-%m-%d"))]
        serializer = GroupedSleepAnalysisSerializer(data=result, many=True)
        serializer.is_valid()
        return Response(serializer.data)


class BodyMassesViewSet(viewsets.ModelViewSet):
    queryset = BodyMass.objects.all()
    serializer_class = BodyMassSerializer
    filter_backends = [LimitFilterBackend]
