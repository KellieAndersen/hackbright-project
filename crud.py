"""CRUD operations"""

from model import db, Recipes, Ingredients, Ratings, Notes,
    Recipe_Tags, Ingredient_Tags, Tag_Recipe_Relation, Recipe_Ingredient_Relation,
    Tag_Ingredient_Relation, connect_to_db
from flask_sqlalchemy import SQLAlchemy


def create_recipe(recipe_name, originator, directions):
    """Create and return a new recipe"""

    recipe = Recipes(recipe_name = recipe_name, originator = originator, directions = directions)

    db.session.add(recipe)
    db.session.commit()

    return recipe


def all_recipes():
    """Return all recipes"""

    return Recipes.query.all()


def get_recipe_by_id(recipe_id):
    """Find recipe using id"""

    return Recipe.query.get(recipe_id)


def create_ingredient(ingredient_name):
    """Create and return a new ingredient"""

    ingredient = Ingredients(ingredient_name = ingredient_name)

    db.session.add(ingredient)
    db.session.commit()

    return ingredient


def all_ingredients():
    """Return all ingredients"""

    return Ingredients.query.all()


def create_rating(recipe, rating):
    """Create and reutrn a new rating"""

    rating = Ratings(recipe = recipe, rating = rating)

    db.session.add(rating)
    db.session.commit()

    return rating


def create_note(recipe, note):
    """Create and return a new note"""

    note = Notes(recipe = recipe, note = note)

    db.session.add(note)
    db.session.commit()

    return note





if __name__ == '__main__':
    from server import app
    connect_to_db(app)