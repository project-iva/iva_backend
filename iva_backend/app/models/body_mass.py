from django.db import models
import uuid


class BodyMass(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    value = models.FloatField()
    recorded_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
