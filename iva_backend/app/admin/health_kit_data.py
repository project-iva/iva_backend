from django.contrib import admin

from iva_backend.app.models import BodyMass


@admin.register(BodyMass)
class BodyMassAdmin(admin.ModelAdmin):
    pass
