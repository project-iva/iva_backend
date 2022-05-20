from django.contrib import admin

from iva_backend.app.models import DayPlanTemplateActivity, DayPlanTemplate, DayPlanActivity, DayPlan


class DayPlanTemplateActivityInlineAdmin(admin.TabularInline):
    model = DayPlanTemplateActivity
    extra = 0


@admin.register(DayPlanTemplate)
class DayPlanTemplateAdmin(admin.ModelAdmin):
    inlines = [DayPlanTemplateActivityInlineAdmin]


class DayPlanActivityInlineAdmin(admin.TabularInline):
    model = DayPlanActivity
    extra = 0


@admin.register(DayPlan)
class DayPlanAdmin(admin.ModelAdmin):
    inlines = [DayPlanActivityInlineAdmin]
