from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=300)
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.CharField(max_length=10)
    total_time = models.CharField(max_length=10)
    calories = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)

    def __str__(self):
        return self.title
