from rest_framework import viewsets

from iva_backend.app.api.serializers.food_serializer import MealSerializer
from iva_backend.app.models import Meal


class MealsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
