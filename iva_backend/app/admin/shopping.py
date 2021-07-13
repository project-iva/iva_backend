from django.contrib import admin

from iva_backend.app.models import ShoppingListRule


@admin.register(ShoppingListRule)
class ShoppingListRuleAdmin(admin.ModelAdmin):
    pass
