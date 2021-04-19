"""Server for recipe app"""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """See homepage"""

    return render_template('homepage.html')


@app.route('/recipes')
def view_recipes():
    """View all recipes"""

    recipes = crud.alphabetical_recipes()
    return render_template('all_recipes.html', see_recipes=recipes)


@app.route('/recipes/<recipe_id>')
def show_recipe(recipe_id):
    """Show recipe details"""

    recipe = crud.get_recipe_by_id(recipe_id)
    return render_template('recipe_details.html', recipe=recipe)


@app.route('/ingredients')
def view_ingredients():
    """View all ingredients"""

    ingredients = crud.alphabetical_ingredients()
    return render_template('all_ingredients.html', see_ingredients=ingredients)


@app.route('/tags')
def view_tags():
    """View all recipe tags"""

    tags =crud.
    return render_template('all_tags.html', see_tags=tags)


@app.route('/ingredients/<ingredient_id>')
def view_recipes_by_ingredient(ingredient_id):
    """Show recipes using a specific ingredient"""

    ingredient = crud.get_ingredient_by_id(ingredient_id)
    recipes_by_ing = crud.get_recipes_by_ingredient(ingredient_id)

    return render_template('ingredient_recipes.html', see_recipes=recipes_by_ing, ingredient=ingredient)##

####
@app.route('/search_recipes')
def search_for_recipes():
    """Show search form"""

    return render_template('search_with_ingredients.html')


@app.route('/search_for_recipes_with_ing', methods=['GET'])
def view_recipes_with_ingredients():
    """Show all the recipes that contain any of the specified ingredients"""

    ingredient_list = request.args.get('ingredients')
    ing_list = crud.string_to_list(ingredient_list)
    ing_id_list = []
    for ingr in ing_list:
        ingred_by_name = crud.get_ingredient_by_name(ingr)
        ing_id_list.append(ingred_by_name.ingredient_id)
    recipe_search_results = crud.get_recipes_by_multiple_ing(ing_id_list)

    return render_template('ing_recipe_search_results.html', see_recipes=recipe_search_results)
####



@app.route('/create_recipe', methods=['POST', 'GET'])
def create_new_recipe():
    """Create a new recipe"""

    if request.method == 'POST':
        recipe_name = request.form.get('recipe_name')
        originator = request.form.get('originator')
        ingredients = request.form.get('ingredients')
        directions = request.form.get('directions')
        notes = request.form.get('notes')
        tags = request.form.get('tags')
        rating = request.form.get('rating')

        created_recipe = crud.create_recipe(recipe_name, originator, directions)
        if notes:
            crud.create_note(created_recipe.recipe_id, notes)

        if rating:
            crud.create_rating(created_recipe.recipe_id, int(rating))

        ing_list = crud.string_to_list(ingredients)
        crud.add_or_create_ing(ing_list, created_recipe)
        ###
        if tags:
            tag_list = crud.string_to_list(tags)
            crud.add_or_create_tag(tag_list, created_recipe)

        ###

        return redirect(f'/recipes/{created_recipe.recipe_id}')

    else:
        return render_template('create_recipe.html')





if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)