from django.shortcuts import render
from .models import Recipe
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

class RecipeList(ListView):
    model = Recipe
    template_name = 'list.html'

class ShowRecipe(DetailView):
    model = Recipe
    template_name = 'show_recipe.html'
