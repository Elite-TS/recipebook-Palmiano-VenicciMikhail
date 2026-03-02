from django.shortcuts import render
from .models import Recipe
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class RecipeList(ListView):
    model = Recipe
    template_name = 'list.html'


class ShowRecipe(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'show_recipe.html'
