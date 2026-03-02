from django.urls import path

from .views import RecipeList, ShowRecipe

app_name = "ledger"

urlpatterns = [
    path('recipes/list', RecipeList.as_view(), name='recipes_list'),
    path('recipe/<int:pk>/', ShowRecipe.as_view(), name='recipe_detail'),
]
