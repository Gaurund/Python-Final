import random

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging
from .forms import RecipeForm, RegisterUserForm
from .models import *

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    template_name = 'cookbookapp/index.html'
    recipes_ = list(Recipe.objects.all())
    recipes_ = random.sample(recipes_, 5)
    context = {
        'title': 'Сайт кулинарных рецептов',
        'recipes': recipes_,
    }

    return render(request, template_name, context)


@login_required
def add_recipe_form(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            steps = form.cleaned_data['steps']
            cook_time = form.cleaned_data['cook_time']
            image = form.cleaned_data['image']
            author = request.user
            recipe = Recipe(
                name=name,
                description=description,
                steps=steps,
                cook_time=cook_time,
                image=image,
                author=author,
            )
            recipe.save()
            if image:
                fs = FileSystemStorage()
                fs.save(image.name, image)
            return redirect(index)


    else:
        form = RecipeForm()
    return render(request, 'cookbookapp/add_recipe.html', {'form': form})


def registration_form(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Регистрация завершена")
            return redirect('index')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/registration.html', {'form': form})


def recipe(request, recipe_id):
    template_name = 'cookbookapp/recipe.html'
    recipe_ = Recipe.objects.get(id=recipe_id)
    categories = RecipeCategory.objects.filter(recipe_id=recipe_id).select_related('category')
    context = {
        'title': 'Рецепт',
        'recipe': recipe_,
        'categories': categories,
    }
    return render(request, template_name, context)


def recipes(request):
    template_name = 'cookbookapp/recipes.html'
    recipes_ = Recipe.objects.all()

    context = {
        'title': 'Список всех рецептов',
        'recipes': recipes_,
    }
    return render(request, template_name, context)


def logout_user(request):
    logout(request)
    messages.success(request, "Вы успешно вышли из системы...")
    return redirect('index')
