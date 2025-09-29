from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def cook(request, dish):
    template_name = 'calculator/index.html'
    recipe = DATA.get(dish)
    if recipe is None:
        return render(request, template_name, {'recipe': {}, 'dish': dish})
    servings = request.GET.get('servings')
    try:
        servings = int(servings)
        if servings < 1:
            servings = 1
    except (TypeError, ValueError):
        servings = 1

    # Умножение ингредиентов на количество порций
    scaled_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    context = {
        'recipe': scaled_recipe,
        'servings':servings,
    }

    return render(request, template_name, context)
