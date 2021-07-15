from django.db import IntegrityError

from iva_backend.app.models import ShoppingList, MeasurableItem, ShoppingListItem
from django.utils import timezone


class ShoppingListManager:
    @staticmethod
    def create_shopping_list() -> ShoppingList:
        # first we close previous shopping list if there is one
        try:
            prev_shopping_list = ShoppingList.objects.get(closed_at=None)
            prev_shopping_list.closed_at = timezone.now()
            prev_shopping_list.save()
        except ShoppingList.DoesNotExist:
            pass
        finally:
            return ShoppingList.objects.create()

    @staticmethod
    def get_or_create_shopping_list() -> ShoppingList:
        try:
            return ShoppingList.objects.get(closed_at=None)
        except ShoppingList.DoesNotExist:
            return ShoppingList.objects.create()

    @staticmethod
    def add_item_on_shopping_list(item: MeasurableItem, amount: float):
        shopping_list = ShoppingListManager.get_or_create_shopping_list()
        try:
            ShoppingListItem.objects.create(shopping_list=shopping_list, item=item, amount=amount)
        except IntegrityError:
            # Item is already on the shopping list
            pass
