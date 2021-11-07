from django.contrib import admin

from iva_backend.app.models import BodyMass, SleepAnalysis, MindfulSession


@admin.register(BodyMass)
class BodyMassAdmin(admin.ModelAdmin):
    pass


@admin.register(SleepAnalysis)
class SleepAnalysisAdmin(admin.ModelAdmin):
    pass


@admin.register(MindfulSession)
class MindfulSessionAdmin(admin.ModelAdmin):
    pass
