from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm

def recipes(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/recipes.html', context)


def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe.html', context)


def createRecipe(request):
    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes')

    context = {'form': form}
    return render(request, 'recipes/recipe_form.html', context)


def updateRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance=recipe)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes')

    context = {'form': form}
    return render(request, 'recipes/recipe_form.html', context)


def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)

    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')

    context = {'recipe': recipe}
    return render(request, 'recipes/delete_recipe.html', context)
