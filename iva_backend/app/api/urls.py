from django.conf.urls import url
from django.urls import path, include
from rest_framework_nested import routers

from iva_backend.app.api.views.assets import AssetsView
from iva_backend.app.api.views.day_plan import CurrentDayPlanView, CurrentDayGoalsView, DayPlanForDateView, \
    DayGoalsForDateView, DayPlansViewSet, DayGoalsListViewSet, DayPlanActivitiesViewSet, DayGoalsViewSet
from iva_backend.app.api.views.food import MealsViewSet, MealTrackingEntriesViewSet, PossibleMealsView, CaloriesGoalView
from iva_backend.app.api.views.health_kit_data import MindfulSessionsViewSet, SleepAnalysesViewSet, BodyMassesViewSet, \
    GroupedSleepAnalysesView, GroupedMindfulSessionsView
from iva_backend.app.api.views.intents import IntentsViewSet
from iva_backend.app.api.views.shopping_list import ShoppingListView, CloseShoppingListView, UpdateShoppingListItemView
from iva_backend.app.api.views.training_instances import TrainingInstancesViewSet, TrainingInstancesExportView

router = routers.SimpleRouter()
router.register(r'intents', IntentsViewSet)
router.register(r'training-instances', TrainingInstancesViewSet)
router.register(r'mindful-sessions', MindfulSessionsViewSet)
router.register(r'sleep-analyses', SleepAnalysesViewSet)
router.register(r'body-masses', BodyMassesViewSet)
router.register(r'meals', MealsViewSet)
router.register(r'meal-tracking-entries', MealTrackingEntriesViewSet)
router.register(r'shopping-list/item', UpdateShoppingListItemView, basename='shopping-list-item')
router.register(r'day-plans', DayPlansViewSet)
router.register(r'day-goals', DayGoalsListViewSet)

day_plans_router = routers.NestedSimpleRouter(router, r'day-plans', lookup='day_plan')
day_plans_router.register(r'activities', DayPlanActivitiesViewSet, basename='day-plan-activities')

day_goals_router = routers.NestedSimpleRouter(router, r'day-goals', lookup='goals_list')
day_goals_router.register(r'goals', DayGoalsViewSet, basename='day-goals')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(day_plans_router.urls)),
    url(r'^', include(day_goals_router.urls)),
    path('export-training-instances/', TrainingInstancesExportView.as_view()),
    path('possible-meals/', PossibleMealsView.as_view()),
    path('shopping-list/', ShoppingListView.as_view()),
    path('shopping-list/close/', CloseShoppingListView.as_view()),
    path('assets/', AssetsView.as_view()),
    path('grouped-sleep-analyses/', GroupedSleepAnalysesView.as_view()),
    path('grouped-mindful-sessions/', GroupedMindfulSessionsView.as_view()),
    path('calories-goal/', CaloriesGoalView.as_view()),
    path('current-day-plan/', CurrentDayPlanView.as_view()),
    url(r'day-plan/(?P<date_string>\d{4}-\d{2}-\d{2})/', DayPlanForDateView.as_view()),
    path('current-day-goals/', CurrentDayGoalsView.as_view()),
    url(r'day-goals/(?P<date_string>\d{4}-\d{2}-\d{2})/', DayGoalsForDateView.as_view()),
]
