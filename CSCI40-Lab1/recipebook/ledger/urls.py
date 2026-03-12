from django.urls import path

from .views import RecipeList, ShowRecipe, RecipeImageUploadView, RecipeCreateView

app_name = "ledger"

urlpatterns = [
    path('recipes/list', RecipeList.as_view(), name='recipes_list'),
    path('recipe/<int:pk>/', ShowRecipe.as_view(), name='recipe_detail'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe_create'),
    path(
        'recipe/<int:pk>/add_image',
        RecipeImageUploadView.as_view(),
        name='recipe_image_upload',
    ),
]
