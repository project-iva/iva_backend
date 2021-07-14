from django.test import TestCase
from django.utils import timezone
from iva_backend.app.models import MeasurableItem
from iva_backend.shopping_list_manager import ShoppingListManager


class PurchasedItemsAreRecordedTestCase(TestCase):
    def test_purchased_items_are_recorded(self):
        shopping_list = ShoppingListManager.get_or_create_shopping_list()
        original_amount = 100
        purchased_amount = 10
        item = MeasurableItem.objects.create(name='item', amount=original_amount, unit=MeasurableItem.Unit.ML)
        ShoppingListManager.add_item_on_shopping_list(item, purchased_amount)
        shopping_list.items.update(purchased=True)
        shopping_list.closed_at = timezone.now()
        shopping_list.save()

        item.refresh_from_db()
        self.assertEquals(item.amount, original_amount + purchased_amount)
