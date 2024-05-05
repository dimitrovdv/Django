from django.urls import path
from calculator.views import calculate_recipe_view

urlpatterns = [
    path('recipes/<recipe_name>/', calculate_recipe_view, name='calculate_recipe')
]
