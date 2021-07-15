from rest_framework import serializers
from iva_backend.app.models import ShoppingListItem, ShoppingList


class ShoppingListItemSerializer(serializers.ModelSerializer):
    item_name = serializers.ReadOnlyField(source='item.name')
    item_unit = serializers.ReadOnlyField(source='item.unit')

    class Meta:
        model = ShoppingListItem
        fields = ['id', 'item_name', 'item_unit', 'amount', 'purchased']


class UpdateShoppingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingListItem
        fields = ['purchased']


class ShoppingListSerializer(serializers.ModelSerializer):
    items = ShoppingListItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingList
        fields = ['items']
