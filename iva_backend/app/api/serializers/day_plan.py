from rest_framework import serializers

from iva_backend.app.models import DayGoals, DayGoal, DayPlanActivity, DayPlan


class DayGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayGoal
        fields = ['__all__']


class DayGoalsSerializer(serializers.ModelSerializer):
    goals = DayGoalSerializer(many=True)

    class Meta:
        model = DayGoals
        fields = ['id', 'date', 'goals']


class DayPlanActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DayPlanActivity
        fields = ['__all__']


class DayPlanSerializer(serializers.ModelSerializer):
    activities = DayPlanActivitySerializer(many=True)

    class Meta:
        model = DayPlan
        fields = ['id', 'date', 'activities']
