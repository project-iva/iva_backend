from django.contrib import admin

from iva_backend.app.models import Ingredient, Meal, MealIngredient, MealTrackerEntry, CaloriesGoal


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


class MealIngredientInlineAdmin(admin.TabularInline):
    model = MealIngredient
    extra = 0


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    readonly_fields = ['kcal']
    inlines = [MealIngredientInlineAdmin]


@admin.register(MealTrackerEntry)
class MealTrackerEntryAdmin(admin.ModelAdmin):
    pass


class MealTrackerEntryInlineAdmin(admin.TabularInline):
    model = MealTrackerEntry
    extra = 0


@admin.register(CaloriesGoal)
class CaloriesGoalAdmin(admin.ModelAdmin):
    inlines = [MealTrackerEntryInlineAdmin]
