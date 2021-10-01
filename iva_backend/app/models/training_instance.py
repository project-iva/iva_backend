from django.db import models
import uuid

from django.utils import timezone

from iva_backend.app.models.intent import Intent


class TrainingInstance(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message_text = models.TextField()
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE, related_name='training_instances')
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
