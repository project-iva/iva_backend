from django.contrib import admin

from iva_backend.app.models import Ingredient, Meal, MealIngredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


class MealIngredientInlineAdmin(admin.TabularInline):
    model = MealIngredient
    extra = 0


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    inlines = [MealIngredientInlineAdmin]

