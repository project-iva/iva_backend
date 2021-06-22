from django.db import models
import uuid


class SleepAnalysis(models.Model):
    class ValueSleepAnalysis(models.IntegerChoices):
        IN_BED = 0
        ASLEEP = 1
        AWAKE = 2

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    source_name = models.CharField(max_length=128)
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(choices=ValueSleepAnalysis.choices)

    class Meta:
        ordering = ('-created_at',)
