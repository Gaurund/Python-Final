from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

User = get_user_model()


# class User(AbstractUser):
#     # first_name = models.CharField(max_length=100)
#     # age = models.DateTimeField(default=timezone.now)
#     pass

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)  # Название
    description = models.TextField()  # Описание
    steps = models.TextField()  # Шаги приготовления
    cook_time = models.DurationField()  # Время приготовления
    image = models.ImageField(upload_to='media', null=True, blank=True)  # Изображение
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор
    categories = models.ManyToManyField(Category, through='RecipeCategory')

    def __str__(self):
        return self.name


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
