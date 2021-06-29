from django.db import models
from django.db.models import UniqueConstraint


class IngredientUnitChoices(models.TextChoices):
    ML = 'ML', 'ml'
    MG = 'MG', 'mg'
    PACKAGE = 'PACKAGE', 'package'


class IngredientKcalPerChoices(models.TextChoices):
    PER_1 = 'PER_1', 'Per 1'
    PER_100 = 'PER_100', 'Per 100'


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
    kcal_per = models.CharField(
        max_length=7,
        choices=IngredientKcalPerChoices.choices,
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

    @property
    def kcal(self) -> float:
        kcal_sum = 0.0
        for ingredient in self.ingredients.all():
            kcal_sum += ingredient.kcal

        return kcal_sum


class MealIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    meal = models.ForeignKey(Meal, related_name='ingredients', on_delete=models.CASCADE)
    amount = models.FloatField()

    @property
    def kcal(self) -> float:
        if self.ingredient.kcal_per == IngredientKcalPerChoices.PER_100:
            return (self.amount / 100) * self.ingredient.kcal

        return self.amount * self.ingredient.kcal
