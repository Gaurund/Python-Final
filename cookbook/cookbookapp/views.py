from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging
from .forms import RecipeForm, LoginForm
from .models import Recipe, User

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    template_name = 'cookbookapp/index.html'
    # logger.info('Shop page accessed')
    recipes = Recipe.objects.all()

    context = {
        'title': 'Сайт кулинарных рецептов',
        'recipes': recipes,
    }

    return render(request, template_name, context)


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


    else:
        form = RecipeForm()
    return render(request, 'cookbookapp/add_recipe.html', {'form': form})


def login_view(request):
    template_name = 'cookbookapp/login.html'
    context = {
        'title': 'Страница входа',
    }

    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User Not Found....')
            return redirect('index')

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or Password does not match...')

    return render(request, template_name, context)
