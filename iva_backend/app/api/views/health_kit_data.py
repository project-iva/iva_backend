from datetime import timedelta
from itertools import groupby
from typing import Optional

from django.db.models import Sum, QuerySet
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from iva_backend.app.api.filter_backends import LimitFilterBackend
from iva_backend.app.api.serializers.health_kit_data import MindfulSessionSerializer, SleepAnalysisSerializer, \
    BodyMassSerializer, GroupedSleepAnalysisSerializer, GroupedMindfulSessionSerializer, BodyMassStatsSerializer
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


class BodyMassStatsView(APIView):
    def get(self, request) -> Response:
        latest_body_mass_measurement = BodyMass.objects.last()
        latest_measurement = latest_body_mass_measurement.value if latest_body_mass_measurement else None

        today = timezone.now()
        week_ago = today - timedelta(weeks=1)
        two_week_ago = today - timedelta(weeks=2)
        month_ago = today - timedelta(weeks=4)
        two_month_ago = today - timedelta(weeks=8)

        past_week_qs = BodyMass.objects.filter(recorded_at__gte=week_ago)
        prev_week_qs = BodyMass.objects.filter(recorded_at__gte=two_week_ago, recorded_at__lt=week_ago)

        past_month_qs = BodyMass.objects.filter(recorded_at__gte=month_ago)
        prev_month_qs = BodyMass.objects.filter(recorded_at__gte=two_month_ago, recorded_at__lt=month_ago)

        week_average = self.__get_average_body_mass(past_week_qs)
        prev_week_average = self.__get_average_body_mass(prev_week_qs)
        month_average = self.__get_average_body_mass(past_month_qs)
        prev_month_average = self.__get_average_body_mass(prev_month_qs)

        serializer = BodyMassStatsSerializer(data={
            'latest_measurement': latest_measurement,
            'week_average': week_average,
            'prev_week_average': prev_week_average,
            'month_average': month_average,
            'prev_month_average': prev_month_average
        })
        serializer.is_valid()
        return Response(serializer.data)

    def __get_average_body_mass(self, queryset: QuerySet) -> Optional[float]:
        if queryset.exists():
            return queryset.aggregate(Sum('value'))['value__sum'] / queryset.count()
        else:
            return None
