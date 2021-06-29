from rest_framework import serializers

from iva_backend.app.models import Meal, MealIngredient


class MealIngredientSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.ReadOnlyField(source='ingredient.name')

    class Meta:
        model = MealIngredient
        fields = ['ingredient_name', 'amount', 'kcal']
        read_only_fields = ['kcal']


class MealSerializer(serializers.ModelSerializer):
    ingredients = MealIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Meal
        fields = ['name', 'type', 'kcal', 'ingredients']
        read_only_fields = ['kcal']
