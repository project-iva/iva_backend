from django.db.models import UniqueConstraint, Sum
from django.utils import timezone
from django.db import models


class Asset(models.Model):
    class Type(models.TextChoices):
        STOCK = 'STOCK', 'Stock'
        CRYPTO = 'CRYPTO', 'Crypto'

    name = models.CharField(max_length=128)
    ticker = models.CharField(max_length=16, unique=True)
    type = models.CharField(
        max_length=6,
        choices=Type.choices,
    )

    @property
    def current_volume(self) -> float:
        return self.order_history.aggregate(Sum('order_volume'))['order_volume__sum']

    def __str__(self):
        return self.name


class AssetOrderHistory(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='order_history')
    order_volume = models.FloatField()
    price = models.FloatField()
    order_date = models.DateTimeField(default=timezone.now)


class AssetTrackerEntry(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='tracker_entries')
    value = models.FloatField()
    market_price = models.FloatField()
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [UniqueConstraint(fields=['asset', 'date'], name='unique_asset_date_entry')]
