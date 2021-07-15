from django.contrib import admin

from iva_backend.app.models import ShoppingListRule, ShoppingList, ShoppingListItem


@admin.register(ShoppingListRule)
class ShoppingListRuleAdmin(admin.ModelAdmin):
    pass


class ShoppingListItemInlineAdmin(admin.TabularInline):
    model = ShoppingListItem
    extra = 0


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    inlines = [ShoppingListItemInlineAdmin]

