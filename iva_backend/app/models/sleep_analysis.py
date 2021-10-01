from django.db import models
from django.utils import timezone


class SleepAnalysis(models.Model):
    class ValueSleepAnalysis(models.IntegerChoices):
        IN_BED = 0
        ASLEEP = 1
        AWAKE = 2

    uuid = models.UUIDField(primary_key=True)
    source_name = models.CharField(max_length=128)
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    value = models.IntegerField(choices=ValueSleepAnalysis.choices)

    @property
    def duration_in_secs(self) -> float:
        return (self.end - self.start).total_seconds()

    class Meta:
        ordering = ('-created_at',)
