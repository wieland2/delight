from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes, name="recipes"),
    path('recipes/<str:pk>/', views.recipe, name="recipe"),

    path('recipes/create/', views.createRecipe, name="create-recipe"),
    path('recipes/<str:pk>/edit/', views.updateRecipe, name="update-recipe"),
    path('recipes/<str:pk>/delete/', views.deleteRecipe, name="delete-recipe"),

]
