from django.test import TestCase
from iva_backend.app.models import Ingredient, MeasurableItem, Meal, MealIngredient, MealTrackerEntry, ShoppingListRule
from iva_backend.shopping_list_manager import ShoppingListManager


class ItemsAreAddedOnShoppingListAutomaticallyTestCase(TestCase):
    def test_items_are_added_on_shopping_list_automatically(self):
        item = MeasurableItem.objects.create(name='item', amount=100, unit=MeasurableItem.Unit.PACKAGE)
        self.check_items_are_added_on_shopping_list_automatically(item)

    def test_ingredients_are_added_on_shopping_list_automatically(self):
        item = Ingredient.objects.create(name='item', amount=100, unit=MeasurableItem.Unit.PACKAGE, kcal=1, kcal_per=Ingredient.KcalPer.PER_100_UNITS)
        self.check_items_are_added_on_shopping_list_automatically(item)

    def check_items_are_added_on_shopping_list_automatically(self, item: MeasurableItem):
        rule = ShoppingListRule.objects.create(item=item, amount_threshold=99, amount_to_purchase=100)

        shopping_list = ShoppingListManager.get_or_create_shopping_list()
        self.assertEquals(shopping_list.items.count(), 0)

        item.amount = 0
        item.save()

        self.assertEquals(shopping_list.items.count(), 1)
        shopping_list_item = shopping_list.items.first()
        self.assertEquals(shopping_list_item.item, item)
        self.assertEquals(shopping_list_item.amount, rule.amount_to_purchase)
