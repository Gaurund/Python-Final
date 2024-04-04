from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('add_recipe/', views.add_recipe_form, name='add_recipe_form'),
    path('login/', views.login_view, name='login_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)