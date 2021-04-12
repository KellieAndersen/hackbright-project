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

    return render_template('all_recipes.html', see_recipes=recipes)


@app.route('/recipes/<recipe_id>')
def show_recipe(recipe_id):
    """Show recipe details"""

    recipe = crud.get_recipe_by_id(recipe_id)
    return render_template('recipe_details.html', recipe=recipe)


@app.route('/ingredients')
def view_ingredients():
    """View all ingredients"""

    return render_template('')


@app.route('/create_recipe')
def create_new_recipe():
    """Create a new recipe"""

    return render_template('')





if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)