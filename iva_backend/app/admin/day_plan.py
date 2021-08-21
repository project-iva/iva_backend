from django.contrib import admin

from iva_backend.app.models import DayPlanTemplateActivity, DayPlanTemplate


class DayPlanTemplateActivityInlineAdmin(admin.TabularInline):
    model = DayPlanTemplateActivity
    extra = 0


@admin.register(DayPlanTemplate)
class DayPlanTemplateAdmin(admin.ModelAdmin):
    inlines = [DayPlanTemplateActivityInlineAdmin]
