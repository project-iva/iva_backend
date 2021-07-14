from django.db import transaction
from django.test import TestCase
from django.utils import timezone

from iva_backend.app.models import ShoppingList, MeasurableItem
from iva_backend.shopping_list_manager import ShoppingListManager


class ShoppingListManagerTestCase(TestCase):
    def test_create_shopping_list(self):
        self.assertEquals(ShoppingList.objects.count(), 0)

        first_shopping_list = ShoppingListManager.create_shopping_list()
        self.assertIsNone(first_shopping_list.closed_at)

        second_shopping_list = ShoppingListManager.create_shopping_list()
        self.assertIsNone(second_shopping_list.closed_at)

        # the shopping lists should be different instances
        self.assertNotEqual(first_shopping_list.pk, second_shopping_list.pk)

        # creating a new shopping list should automatically close the previous list
        first_shopping_list.refresh_from_db()
        self.assertIsNotNone(first_shopping_list.closed_at)

    def test_get_or_create_shopping_list(self):
        self.assertEquals(ShoppingList.objects.count(), 0)

        first_shopping_list = ShoppingListManager.get_or_create_shopping_list()
        self.assertIsNone(first_shopping_list.closed_at)

        second_shopping_list = ShoppingListManager.get_or_create_shopping_list()
        self.assertIsNone(second_shopping_list.closed_at)

        # the shopping lists should be the same instances
        self.assertEquals(first_shopping_list.pk, second_shopping_list.pk)

        # the shopping list should still be open
        first_shopping_list.refresh_from_db()
        self.assertIsNone(first_shopping_list.closed_at)

        first_shopping_list.closed_at = timezone.now()
        first_shopping_list.save()

        third_shopping_list = ShoppingListManager.get_or_create_shopping_list()
        self.assertIsNone(second_shopping_list.closed_at)
        # after the first shopping list has been closed, now a new shopping list should be created instead
        self.assertNotEqual(first_shopping_list.pk, third_shopping_list.pk)

    def test_add_item_on_shopping_list(self):
        shopping_list = ShoppingListManager.get_or_create_shopping_list()
        self.assertEquals(shopping_list.items.count(), 0)

        item = MeasurableItem.objects.create(name='item', amount=100, unit=MeasurableItem.Unit.ML)

        # add item on the list
        amount = 10
        ShoppingListManager.add_item_on_shopping_list(item, amount)
        self.assertEquals(shopping_list.items.count(), 1)
        shopping_item = shopping_list.items.first()
        self.assertEquals(shopping_item.item, item)
        self.assertEquals(shopping_item.amount, amount)

        # each test is wrapped in a transaction so after an IntegrityError all the other queries will fail
        # we can avoid that by wrapping the statement in an atomic block
        with transaction.atomic():
            # try adding the same item again
            ShoppingListManager.add_item_on_shopping_list(item, amount)
        # it should still be there only once and the amount should not change

        self.assertEquals(shopping_list.items.count(), 1)
        self.assertEquals(shopping_list.items.first().amount, amount)
