import datetime

from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet

from iva_backend.app.api.serializers.day_plan import DayGoalsSerializer, DayPlanSerializer, DayPlanActivitySerializer, \
    DayGoalSerializer, DayPlanTemplateSerializer, DayPlanTemplateActivitySerializer, PatchDayPlanTemplateSerializer
from iva_backend.app.models import DayGoals, DayPlan, DayPlanActivity, DayGoal, DayPlanTemplate, DayPlanTemplateActivity


class DayPlansViewSet(ReadOnlyModelViewSet):
    queryset = DayPlan.objects.all()
    serializer_class = DayPlanSerializer


class DayPlanActivitiesViewSet(ModelViewSet):
    serializer_class = DayPlanActivitySerializer

    def get_queryset(self):
        return DayPlanActivity.objects.filter(day_plan=self.kwargs.get('day_plan_pk'))

    def perform_create(self, serializer):
        day_plan = DayPlan.objects.get(pk=self.kwargs.get('day_plan_pk'))
        serializer.save(day_plan=day_plan)


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


class DayPlanTemplatesViewSet(mixins.CreateModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.ListModelMixin,
                              GenericViewSet):
    queryset = DayPlanTemplate.objects.all()

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return PatchDayPlanTemplateSerializer

        return DayPlanTemplateSerializer


class DayPlanTemplateActivitiesViewSet(ModelViewSet):
    serializer_class = DayPlanTemplateActivitySerializer

    def get_queryset(self):
        return DayPlanTemplateActivity.objects.filter(day_plan_template=self.kwargs.get('day_plan_template_pk'))

    def perform_create(self, serializer):
        day_plan_template = DayPlanTemplate.objects.get(pk=self.kwargs.get('day_plan_template_pk'))
        serializer.save(day_plan_template=day_plan_template)


class DayPlanFromTemplateView(APIView):
    def post(self, request, day_plan_pk, day_plan_template_pk) -> Response:
        day_plan = get_object_or_404(DayPlan, pk=day_plan_pk)
        day_plan_template = get_object_or_404(DayPlanTemplate, pk=day_plan_template_pk)

        for activity in day_plan_template.activities.all():
            DayPlanActivity.objects.create(
                start_time=activity.start_time,
                end_time=activity.end_time,
                name=activity.name,
                description=activity.description,
                type=activity.type,
                day_plan=day_plan,
            )

        serializer = DayPlanSerializer(day_plan)
        return Response(serializer.data)


class DayGoalsListViewSet(ReadOnlyModelViewSet):
    queryset = DayGoals.objects.all()
    serializer_class = DayGoalsSerializer


class DayGoalsViewSet(ModelViewSet):
    serializer_class = DayGoalSerializer

    def get_queryset(self):
        return DayGoal.objects.filter(goals_list=self.kwargs.get('goals_list_pk'))

    def perform_create(self, serializer):
        goals = DayGoals.objects.get(pk=self.kwargs.get('goals_list_pk'))
        serializer.save(goals_list=goals)


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
