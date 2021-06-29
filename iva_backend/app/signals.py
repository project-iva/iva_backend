from django.db.models.signals import post_save
from django.dispatch import receiver

from iva_backend.app.iva_service.iva_service import IvaService
from iva_backend.app.models import MindfulSession
from iva_backend.app.models import MealTrackerEntry


@receiver(post_save, sender=MindfulSession)
def mindful_session_saved_signal(sender, instance, created, **kwargs):
    if created:
        iva_service = IvaService()
        iva_service.send_mindful_session_created_notification()


@receiver(post_save, sender=MealTrackerEntry)
def subtract_used_ingredients(sender, instance, created, **kwargs):
    if created:
        # subtracts used up ingredients in the meal
        for meal_ingredient in instance.meal.ingredients.all():
            ingredient = meal_ingredient.ingredient
            ingredient.amount -= meal_ingredient.amount
            ingredient.save()
