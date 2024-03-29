from django.http import Http404
from rest_framework import viewsets, mixins, status, views
from rest_framework.response import Response

from iva_backend.app.api.serializers.food import MealSerializer, MealTrackerEntrySerializer, \
    CreateMealTrackerEntrySerializer, CaloriesGoalSerializer
from iva_backend.app.models import Meal, MealTrackerEntry, CaloriesGoal


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


class PossibleMealsView(views.APIView):
    def get(self, request):
        possible_meals = list(filter(lambda meal: meal.can_be_prepared, Meal.objects.all()))
        meal_serializer = MealSerializer(possible_meals, many=True)
        return Response(meal_serializer.data)


class CaloriesGoalView(views.APIView):
    def get(self, request):
        try:
            goal = CaloriesGoal.objects.latest('id')
        except CaloriesGoal.DoesNotExist:
            raise Http404('No calories goal has been set')

        calories_goal_serializer = CaloriesGoalSerializer(goal)
        return Response(calories_goal_serializer.data)
