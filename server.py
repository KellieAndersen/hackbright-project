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

    return render_template('')


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