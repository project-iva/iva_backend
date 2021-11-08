from django.contrib import admin

from iva_backend.app.models import Intent


@admin.register(Intent)
class IntentAdmin(admin.ModelAdmin):
    pass
