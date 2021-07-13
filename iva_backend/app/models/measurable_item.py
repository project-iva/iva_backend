from polymorphic.models import PolymorphicModel
from django.db import models


class MeasurableItem(PolymorphicModel):
    class Unit(models.TextChoices):
        ML = 'ML', 'ml'
        MG = 'MG', 'mg'
        PACKAGE = 'PACKAGE', 'package'

    amount = models.FloatField()
    unit = models.CharField(
        max_length=7,
        choices=Unit.choices,
    )
