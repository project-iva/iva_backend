from django.db import models
from django.utils import timezone
from iva_backend.app.models.measurable_item import MeasurableItem


class Ingredient(MeasurableItem):
    class KcalPer(models.TextChoices):
        PER_1_UNIT = 'PER_1_UNIT', 'Per 1 unit'
        PER_100_UNITS = 'PER_100_UNITS', 'Per 100 units'

    kcal = models.IntegerField()
    kcal_per = models.CharField(
        max_length=13,
        choices=KcalPer.choices,
    )

    def __str__(self) -> str:
        return self.name


class Meal(models.Model):
    class Type(models.TextChoices):
        BREAKFAST = 'BREAKFAST', 'Breakfast'
        LUNCH = 'LUNCH', 'Lunch'
        DINNER = 'DINNER', 'Dinner'
        SNACK = 'SNACK', 'Snack'

    name = models.CharField(max_length=128, unique=True)
    type = models.CharField(
        max_length=9,
        choices=Type.choices,
    )

    def __str__(self) -> str:
        return self.name

    @property
    def kcal(self) -> float:
        kcal_sum = 0.0
        for ingredient in self.ingredients.all():
            kcal_sum += ingredient.kcal

        return kcal_sum

    @property
    def can_be_prepared(self) -> bool:
        """
        Checks if the meal can be prepared with the currently available ingredients
        """
        for meal_ingredient in self.ingredients.all():
            if not meal_ingredient.is_available:
                return False
        return True


class MealIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    meal = models.ForeignKey(Meal, related_name='ingredients', on_delete=models.CASCADE)
    amount = models.FloatField()

    @property
    def kcal(self) -> float:
        if self.ingredient.kcal_per == Ingredient.KcalPer.PER_100_UNITS:
            return (self.amount / 100) * self.ingredient.kcal

        return self.amount * self.ingredient.kcal

    @property
    def is_available(self) -> bool:
        return self.ingredient.amount >= self.amount


class MealTrackerEntry(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.PROTECT)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Meal tracker entries'
