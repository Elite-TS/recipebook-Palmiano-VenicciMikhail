from django.urls import path

from .views import RecipeList, ShowRecipe

app_name = "ledger"

urlpatterns = [
    # path('recipe/1', recipe1, name='recipe1'),
    # path('recipe/2', recipe2, name='recipe2'),
    # path('recipes/list', recipes_list, name='recipes_list')
    path('recipes/list', RecipeList.as_view(), name='recipes_list'),
    path('<int:pk>/', ShowRecipe.as_view(), name='recipe_detail'),
]
