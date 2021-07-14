from django.db.models.signals import post_save
from django.dispatch import receiver

from iva_backend.app.models import MealTrackerEntry


@receiver(post_save, sender=MealTrackerEntry)
def subtract_used_ingredients(sender, instance, created, **kwargs):
    if created:
        # subtracts used up ingredients in the meal
        for meal_ingredient in instance.meal.ingredients.all():
            ingredient = meal_ingredient.ingredient
            ingredient.amount -= meal_ingredient.amount
            ingredient.save()
