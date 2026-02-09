from django.urls import path

from .views import recipe1, recipe2, recipes_list

app_name = "ledger"

urlpatterns = [
    path('recipe/1', recipe1, name='recipe1'),
    path('recipe/2', recipe2, name='recipe2'),
    path('recipes/list', recipes_list, name='recipes_list')
]
