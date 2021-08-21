from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from iva_backend.app.iva_service.iva_service import IvaService
from iva_backend.app.models import DayPlanActivity


@receiver(post_save, sender=DayPlanActivity)
def notify_iva_about_day_plan_change(sender, instance, **kwargs):
    # send notification only if the current day plan has been changed
    if instance.day_plan.date == timezone.now().date():
        IvaService.send_day_plan_changed_notification()
