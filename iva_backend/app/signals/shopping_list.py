from django.db.models.signals import post_save
from django.dispatch import receiver
from iva_backend.app.models import Ingredient, ShoppingListRule
from iva_backend.shopping_list_manager import ShoppingListManager


@receiver(post_save, sender=Ingredient)
def check_if_ingredient_needs_to_be_added_to_shopping_list(sender, instance, **kwargs):
    try:
        rule = instance.shopping_list_rule
    except ShoppingListRule.DoesNotExist:
        pass
    else:
        if rule.item_should_be_added_to_shopping_list:
            ShoppingListManager.add_item_on_shopping_list(instance, rule.amount_to_purchase)
