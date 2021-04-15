"""Server for recipe app"""

from flask import (Flask, render_template, request, flash, session, redirect)
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


@app.route('/ingredients/<ingredient_id>')
def view_recipes_by_ingredient(ingredient_id):
    """Show recipes using a specific ingredient"""

    ingredient = crud.get_ingredient_by_id(ingredient_id)
    recipes_by_ing = crud.get_recipes_by_ingredient(ingredient_id)

    return render_template('ingredient_recipes.html', see_recipes=recipes_by_ing, ingredient=ingredient)##



@app.route('/create_recipe', methods=['GET'])
def create_new_recipe():
    """Create a new recipe"""

    recipe_name = request.args.get('recipe_name')
    originator = request.args.get('originator')
    ingredients = request.args.get('ingredients')
    directions = request.args.get('directions')
    notes = request.args.get('notes')
    tags = request.args.get('tags')
    rating = request.args.get('rating')
    

    return render_template('create_recipe.html')##





if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)