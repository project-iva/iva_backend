from django.db import models
from django.db.models import UniqueConstraint

from iva_backend.app.models.measurable_item import MeasurableItem


class ShoppingListRule(models.Model):
    item = models.ForeignKey(MeasurableItem, on_delete=models.CASCADE)
    amount_threshold = models.FloatField()

    def __str__(self) -> str:
        return self.item.name

    def item_should_be_added_to_shopping_list(self) -> bool:
        return self.item.amount < self.amount_threshold

    class Meta:
        constraints = [UniqueConstraint(fields=['item'], name='unique_item_rule')]
