from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from iva_backend.app.api.serializers.food_serializer import MealSerializer, MealTrackerEntrySerializer, \
    CreateMealTrackerEntrySerializer
from iva_backend.app.models import Meal, MealTrackerEntry


class MealsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MealTrackingEntriesViewSet(mixins.CreateModelMixin,
                                 mixins.ListModelMixin,
                                 viewsets.GenericViewSet):
    queryset = MealTrackerEntry.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateMealTrackerEntrySerializer

        return MealTrackerEntrySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # after the entry was created, return detailed response
        instance_serializer = MealTrackerEntrySerializer(serializer.instance)
        return Response(instance_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
