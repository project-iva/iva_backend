from django.db import models
from django.utils import timezone


class BodyMass(models.Model):
    uuid = models.UUIDField(primary_key=True)
    value = models.FloatField()
    recorded_at = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at',)
