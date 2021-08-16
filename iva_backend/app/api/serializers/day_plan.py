from rest_framework import serializers

from iva_backend.app.models import DayGoals, DayGoal, DayPlanActivity, DayPlan


class DayGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayGoal
        exclude = ['goals_list']


class DayGoalsSerializer(serializers.ModelSerializer):
    goals = DayGoalSerializer(many=True)

    class Meta:
        model = DayGoals
        fields = ['id', 'date', 'goals']


class DayPlanActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DayPlanActivity
        exclude = ['day_plan']


class DayPlanSerializer(serializers.ModelSerializer):
    activities = DayPlanActivitySerializer(many=True)

    class Meta:
        model = DayPlan
        fields = ['id', 'date', 'activities']
