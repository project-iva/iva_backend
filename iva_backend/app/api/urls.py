from django.conf.urls import url
from django.urls import path, include
from rest_framework_nested import routers

from iva_backend.app.api.views.assets import AssetsView
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

urlpatterns = [
    url(r'^', include(router.urls)),
    path('export-training-instances/', TrainingInstancesExportView.as_view()),
    path('possible-meals/', PossibleMealsView.as_view()),
    path('shopping-list/', ShoppingListView.as_view()),
    path('shopping-list/close/', CloseShoppingListView.as_view()),
    path('assets/', AssetsView.as_view()),
    path('grouped-sleep-analyses/', GroupedSleepAnalysesView.as_view()),
    path('grouped-mindful-sessions/', GroupedMindfulSessionsView.as_view()),
    path('calories-goal/', CaloriesGoalView.as_view())
]
