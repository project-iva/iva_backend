from rest_framework import viewsets, mixins

from iva_backend.app.api.serializers.food_serializer import MealSerializer, MealTrackerEntrySerializer
from iva_backend.app.models import Meal, MealTrackerEntry


class MealsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MealTrackingEntriesViewSet(mixins.CreateModelMixin,
                                 mixins.ListModelMixin,
                                 viewsets.GenericViewSet):
    queryset = MealTrackerEntry.objects.all()
    serializer_class = MealTrackerEntrySerializer
