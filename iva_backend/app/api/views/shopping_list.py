from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from iva_backend.app.api.serializers.shopping_list import ShoppingListSerializer, UpdateShoppingListItemSerializer
from iva_backend.shopping_list_manager import ShoppingListManager


class ShoppingListView(APIView):
    def get(self, request):
        shopping_list = ShoppingListManager.get_or_create_shopping_list()
        serializer = ShoppingListSerializer(shopping_list)
        return Response(serializer.data)


class CloseShoppingListView(APIView):
    def get(self, request):
        # closes last shopping list and creates a new one
        shopping_list = ShoppingListManager.create_shopping_list()
        serializer = ShoppingListSerializer(shopping_list)
        return Response(serializer.data)


class UpdateShoppingListItemView(mixins.UpdateModelMixin,
                                 viewsets.GenericViewSet):
    serializer_class = UpdateShoppingListItemSerializer

    def get_queryset(self):
        return ShoppingListManager.get_or_create_shopping_list().items
