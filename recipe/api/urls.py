from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
     url(r'^recipes/(?P<pk>[0-9]+)$', views.RecipeApiView.as_view(), name='recipes'),
     url(r'^recipes/$', views.RecipeApiView.as_view(), name='recipes'),
]