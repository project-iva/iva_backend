from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from iva_backend.app.models import MealTrackerEntry, CaloriesGoal


@receiver(post_save, sender=MealTrackerEntry)
def subtract_used_ingredients(sender, instance, created, **kwargs):
    if created:
        # subtracts used up ingredients in the meal
        for meal_ingredient in instance.meal.ingredients.all():
            ingredient = meal_ingredient.ingredient
            ingredient.amount -= meal_ingredient.amount
            ingredient.save()


@receiver(post_save, sender=MealTrackerEntry)
def set_current_calories_goal(sender, instance, created, **kwargs):
    if created:
        # set the current calories goal
        try:
            calories_goal = CaloriesGoal.objects.latest('id')
        except CaloriesGoal.DoesNotExist:
            pass
        else:
            instance.calories_goal = calories_goal
            instance.save()


@receiver(post_save, sender=CaloriesGoal)
def set_end_date_on_previous_calories_goal(sender, instance, created, **kwargs):
    if created:
        # if there is an existing calories goal, set the end date
        try:
            previous_calories_goal = CaloriesGoal.objects.exclude(pk=instance.pk).get(end=None)
        except CaloriesGoal.DoesNotExist:
            # if there is not one, then there is nothing to do
            pass
        else:
            previous_calories_goal.end = timezone.now()
            previous_calories_goal.save()
