from django.shortcuts import render
from django.http import Http404, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Recipe
from .recipeSerializer import RecipeSerializer
from rest_framework import status, generics, mixins, exceptions, viewsets


class RecipeApiView(generics.GenericAPIView,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin):

    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)
