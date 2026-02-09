from django.urls import path

from .views import recipe1

app_name = "ledger"

urlpatterns = [
    path('recipe/1', recipe1, name='recipe1'),
]
