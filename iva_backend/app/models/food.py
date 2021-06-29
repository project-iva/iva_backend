from django.db import models
from django.db.models import UniqueConstraint


class IngredientUnitChoices(models.TextChoices):
    ML = 'ML', 'ml'
    MG = 'MG', 'mg'
    PACKAGE = 'PACKAGE', 'package'


class IngredientKcalUnitChoices(models.TextChoices):
    PER_100_ML = 'PER_100_ML', 'Per 100 ml'
    PER_100_MG = 'PER_100_MG', 'Per 100 mg'
    PER_PACKAGE = 'PER_PACKAGE', 'Per package'


class MealTypeChoices(models.TextChoices):
    BREAKFAST = 'BREAKFAST', 'Breakfast'
    LUNCH = 'LUNCH', 'Lunch'
    DINNER = 'DINNER', 'Dinner'
    SNACK = 'SNACK', 'Snack'


class Ingredient(models.Model):
    name = models.CharField(max_length=128)
    amount = models.FloatField()
    unit = models.CharField(
        max_length=7,
        choices=IngredientUnitChoices.choices,
    )
    kcal = models.IntegerField()
    kcal_per_unit = models.CharField(
        max_length=11,
        choices=IngredientKcalUnitChoices.choices,
    )

    class Meta:
        constraints = [UniqueConstraint(fields=['name'], name='unique_ingredient')]

    def __str__(self) -> str:
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(
        max_length=9,
        choices=MealTypeChoices.choices,
    )

    class Meta:
        constraints = [UniqueConstraint(fields=['name'], name='unique_meal')]

    def __str__(self) -> str:
        return self.name


class MealIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    meal = models.ForeignKey(Meal, related_name='ingredients', on_delete=models.CASCADE)
    amount = models.FloatField()
