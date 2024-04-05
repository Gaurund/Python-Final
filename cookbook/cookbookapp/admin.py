from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


class RecipeInlineAdmin(admin.TabularInline):
    model = Recipe.categories.through
    list_display = [
        'name',
    ]

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    inlines = (RecipeInlineAdmin,)
