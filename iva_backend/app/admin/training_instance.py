from django.contrib import admin

from iva_backend.app.models import TrainingInstance


@admin.action(description='Mark selected training instances as approved')
def mark_approved(admin, request, queryset):
    queryset.update(approved=True)


@admin.register(TrainingInstance)
class TrainingInstanceAdmin(admin.ModelAdmin):
    actions = [mark_approved]
