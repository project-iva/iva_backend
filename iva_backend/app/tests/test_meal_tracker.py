from django.test import TestCase
from iva_backend.app.models import Ingredient, MeasurableItem, Meal, MealIngredient, MealTrackerEntry


class MealTrackerTestCase(TestCase):
    def setUp(self):
        self.ingredient_1_original_amount = 100
        self.ingredient_1 = Ingredient.objects.create(
            name='Ingredient 1',
            kcal=1,
            nutrition_per=Ingredient.NutritionPer.PER_100_UNITS,
            amount=self.ingredient_1_original_amount,
            unit=MeasurableItem.Unit.MG
        )

        self.ingredient_2_original_amount = 200
        self.ingredient_2 = Ingredient.objects.create(
            name='Ingredient 2',
            kcal=1,
            nutrition_per=Ingredient.NutritionPer.PER_100_UNITS,
            amount=self.ingredient_2_original_amount,
            unit=MeasurableItem.Unit.MG
        )

        self.meal = Meal.objects.create(name='self.meal', type=Meal.Type.LUNCH)
        self.meal_ingredient_1 = MealIngredient.objects.create(ingredient=self.ingredient_1, meal=self.meal, amount=1)
        self.meal_ingredient_2 = MealIngredient.objects.create(ingredient=self.ingredient_2, meal=self.meal, amount=2)

    def test_subtracting_used_ingredients(self):
        MealTrackerEntry.objects.create(meal=self.meal)

        self.ingredient_1.refresh_from_db()
        self.ingredient_2.refresh_from_db()

        expected_new_ingredient_1_amount = self.ingredient_1_original_amount - self.meal_ingredient_1.amount
        self.assertEquals(self.ingredient_1.amount, expected_new_ingredient_1_amount)

        expected_new_ingredient_2_amount = self.ingredient_2_original_amount - self.meal_ingredient_2.amount
        self.assertEquals(self.ingredient_2.amount, expected_new_ingredient_2_amount)
