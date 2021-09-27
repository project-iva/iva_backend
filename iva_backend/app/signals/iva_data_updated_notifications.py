from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from iva_backend.app.iva_service.iva_service import IvaService
from iva_backend.app.models import DayPlanActivity, DayGoal, CaloriesGoal, MealTrackerEntry, BodyMass, SleepAnalysis, \
    MindfulSession


@receiver(post_save, sender=DayPlanActivity)
def notify_iva_about_day_plan_update(sender, instance, **kwargs):
    # send notification only if the current day plan has been updated
    if instance.day_plan.date == timezone.now().date():
        IvaService.send_data_updated_notification(IvaService.DataUpdatedType.DAY_PLAN)


@receiver(post_save, sender=DayGoal)
def notify_iva_about_day_goal_update(sender, instance, **kwargs):
    # send notification only if the day goal is from today's list
    if instance.goals_list.date == timezone.now().date():
        IvaService.send_data_updated_notification(IvaService.DataUpdatedType.DAY_GOALS)


@receiver(post_save, sender=CaloriesGoal)
def notify_iva_about_calories_goal_update(sender, instance, **kwargs):
    IvaService.send_data_updated_notification(IvaService.DataUpdatedType.CALORIES)


@receiver(post_save, sender=MealTrackerEntry)
def notify_iva_about_calories_update(sender, instance, created, **kwargs):
    if created:
        IvaService.send_data_updated_notification(IvaService.DataUpdatedType.CALORIES)


@receiver(post_save, sender=BodyMass)
def notify_iva_about_body_mass_update(sender, instance, **kwargs):
    IvaService.send_data_updated_notification(IvaService.DataUpdatedType.BODY_MASS)


@receiver(post_save, sender=SleepAnalysis)
def notify_iva_about_sleep_analysis_update(sender, instance, **kwargs):
    IvaService.send_data_updated_notification(IvaService.DataUpdatedType.SLEEP)


@receiver(post_save, sender=MindfulSession)
def notify_iva_about_mindful_session_update(sender, instance, **kwargs):
    IvaService.send_data_updated_notification(IvaService.DataUpdatedType.MINDFUL_SESSIONS)
