from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from iva_backend.app.models import ShoppingListRule, MeasurableItem, ShoppingListItem
from iva_backend.app.polymorphic_receiver import polymorphic_receiver
from iva_backend.shopping_list_manager import ShoppingListManager


@polymorphic_receiver(post_save, sender=MeasurableItem)
def check_if_item_needs_to_be_added_to_shopping_list(sender, instance, **kwargs):
    try:
        rule = instance.shopping_list_rule
    except ShoppingListRule.DoesNotExist:
        pass
    else:
        if rule.item_should_be_added_to_shopping_list:
            ShoppingListManager.add_item_on_shopping_list(instance, rule.amount_to_purchase)
