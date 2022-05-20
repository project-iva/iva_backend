from rest_framework import serializers

from iva_backend.app.models import DayGoals, DayGoal, DayPlanActivity, DayPlan, DayPlanTemplateActivity, DayPlanTemplate


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


class DayPlanTemplateActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DayPlanTemplateActivity
        exclude = ['day_plan_template']


class DayPlanTemplateSerializer(serializers.ModelSerializer):
    activities = DayPlanTemplateActivitySerializer(many=True)

    def create(self, validated_data):
        activities = validated_data.pop('activities')
        day_plan_template = DayPlanTemplate.objects.create(**validated_data)
        for activity in activities:
            DayPlanTemplateActivity.objects.create(day_plan_template=day_plan_template, **activity)
        return day_plan_template

    class Meta:
        model = DayPlanTemplate
        fields = ['id', 'name', 'activities']


class PatchDayPlanTemplateSerializer(serializers.ModelSerializer):
    activities = DayPlanTemplateActivitySerializer(many=True, read_only=True)

    class Meta:
        model = DayPlanTemplate
        fields = ['id', 'name', 'activities']
