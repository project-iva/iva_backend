import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from iva_backend.app.api.serializers.day_plan import DayGoalsSerializer, DayPlanSerializer, DayPlanActivitySerializer, \
    DayGoalSerializer
from iva_backend.app.models import DayGoals, DayPlan, DayPlanActivity, DayGoal


class DayPlansViewSet(ReadOnlyModelViewSet):
    queryset = DayPlan.objects.all()
    serializer_class = DayPlanSerializer


class DayPlanActivitiesViewSet(ModelViewSet):
    serializer_class = DayPlanActivitySerializer

    def get_queryset(self):
        return DayPlanActivity.objects.filter(day_plan=self.kwargs.get('day_plan_pk'))


class CurrentDayPlanView(APIView):
    def get(self, request) -> Response:
        day_plan = DayPlan.get_current_day_plan()
        serializer = DayPlanSerializer(day_plan)
        return Response(serializer.data)


class DayPlanForDateView(APIView):
    def get(self, request, date_string) -> Response:
        date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
        day_plan = DayPlan.get_day_plan_for_date(date)
        serializer = DayPlanSerializer(day_plan)
        return Response(serializer.data)


class DayGoalsListViewSet(ReadOnlyModelViewSet):
    queryset = DayGoals.objects.all()
    serializer_class = DayGoalsSerializer


class DayGoalsViewSet(ModelViewSet):
    serializer_class = DayGoalSerializer

    def get_queryset(self):
        return DayGoal.objects.filter(goals_list=self.kwargs.get('goals_list_pk'))


class CurrentDayGoalsView(APIView):
    def get(self, request) -> Response:
        day_goals = DayGoals.get_current_day_goals_list()
        serializer = DayGoalsSerializer(day_goals)
        return Response(serializer.data)


class DayGoalsForDateView(APIView):
    def get(self, request, date_string) -> Response:
        date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
        day_goals = DayGoals.get_day_goals_list_for_date(date)
        serializer = DayGoalsSerializer(day_goals)
        return Response(serializer.data)
