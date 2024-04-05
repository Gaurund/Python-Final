from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('add_recipe/', views.add_recipe_form, name='add_recipe_form'),
    path('recipe/<int:recipe_id>/', views.recipe, name="recipe_id"),
    path('recipes/', views.recipes, name="recipes"),
    # path('login/', views.login_view, name='login_view'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('registration/', views.registration_form, name='registration_form')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
