from .models import Recipe
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id',
                  'title',
                  'image_url',
                  'ingredients',
                  'instructions',
                  'prep_time',
                  'total_time',
                  'calories',
                  'protein',
                  'carbs',
                  'fat'
                  )