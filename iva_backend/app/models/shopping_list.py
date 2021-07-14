from django.db import models
from django.db.models import UniqueConstraint
from django.utils import timezone
from iva_backend.app.models.measurable_item import MeasurableItem


class ShoppingListRule(models.Model):
    item = models.OneToOneField(
        MeasurableItem,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='shopping_list_rule'
    )
    amount_threshold = models.FloatField()
    amount_to_purchase = models.FloatField()

    def __str__(self) -> str:
        return self.item.name

    def item_should_be_added_to_shopping_list(self) -> bool:
        return self.item.amount < self.amount_threshold


class ShoppingList(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    closed_at = models.DateTimeField(null=True, blank=True)


class ShoppingListItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(MeasurableItem, on_delete=models.CASCADE)
    amount = models.FloatField()
    purchased = models.BooleanField(default=False)

    class Meta:
        constraints = [UniqueConstraint(fields=['shopping_list', 'item'], name='unique_item_on_a_shopping_list')]
