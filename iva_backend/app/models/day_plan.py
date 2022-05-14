from __future__ import annotations
from django.db import models
from django.utils import timezone
import datetime


class DayGoals(models.Model):
    date = models.DateField(unique=True)

    @staticmethod
    def get_day_goals_list_for_date(day_goal_date: datetime.date) -> DayGoals:
        day_goal_list, _ = DayGoals.objects.get_or_create(date=day_goal_date)
        return day_goal_list

    @staticmethod
    def get_current_day_goals_list() -> DayGoals:
        return DayGoals.get_day_goals_list_for_date(timezone.now().date())


class DayGoal(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    finished = models.BooleanField(default=False)
    goals_list = models.ForeignKey(DayGoals, related_name='goals', on_delete=models.CASCADE)


class DayPlan(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return self.date.strftime("%d/%m/%Y")

    @staticmethod
    def get_day_plan_for_date(day_plan_date: datetime.date) -> DayPlan:
        day_plan, _ = DayPlan.objects.get_or_create(date=day_plan_date)
        return day_plan

    @staticmethod
    def get_current_day_plan() -> DayPlan:
        return DayPlan.get_day_plan_for_date(timezone.now().date())


class Activity(models.Model):
    class Type(models.TextChoices):
        MORNING_ROUTINE = 'MORNING_ROUTINE', 'Morning routine'
        EVENING_ROUTINE = 'EVENING_ROUTINE', 'Evening routine'
        MEAL = 'MEAL', 'Meal'
        SCHOOL = 'SCHOOL', 'School'
        LEISURE = 'LEISURE', 'Leisure'
        WORKOUT = 'WORKOUT', 'Workout'
        JOB = 'JOB', 'Job'
        HOBBY = 'HOBBY', 'Hobby'
        OTHER = 'OTHER', 'Other'

    start_time = models.TimeField()
    end_time = models.TimeField()
    name = models.CharField(max_length=256)
    description = models.TextField()
    type = models.CharField(max_length=15, choices=Type.choices, default=Type.OTHER)

    class Meta:
        abstract = True
        ordering = ['start_time']


class DayPlanActivity(Activity):
    started_at = models.TimeField(blank=True, null=True, default=None)
    ended_at = models.TimeField(blank=True, null=True, default=None)
    skipped = models.BooleanField(default=False)
    day_plan = models.ForeignKey(DayPlan, related_name='activities', on_delete=models.CASCADE)


class DayPlanTemplate(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class DayPlanTemplateActivity(Activity):
    day_plan_template = models.ForeignKey(DayPlanTemplate, related_name='activities', on_delete=models.CASCADE)
