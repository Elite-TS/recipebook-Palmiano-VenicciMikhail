from django.urls import path

from .views import recipe1, recipe2, recipes_list, RecipeListView, RecipeDetailView

app_name = "ledger"

urlpatterns = [
    # path('recipe/1', recipe1, name='recipe1'),
    # path('recipe/2', recipe2, name='recipe2'),
    # path('recipes/list', recipes_list, name='recipes_list')
    path('recipes/list', RecipeListView.as_view(), name='recipes_list'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
]
