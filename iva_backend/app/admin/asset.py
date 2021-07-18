from django.contrib import admin

from iva_backend.app.models import AssetOrderHistory, Asset, AssetTrackerEntry


class AssetOrderHistoryInlineAdmin(admin.TabularInline):
    model = AssetOrderHistory
    extra = 0


class AssetTrackerEntryInlineAdmin(admin.TabularInline):
    model = AssetTrackerEntry
    extra = 0


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    inlines = [AssetOrderHistoryInlineAdmin, AssetTrackerEntryInlineAdmin]
