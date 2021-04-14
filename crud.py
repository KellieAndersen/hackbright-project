"""CRUD operations"""

from model import db, Recipes, Ingredients, Ratings, Notes, Recipe_Tags, Tag_Recipe_Relation, connect_to_db
from flask_sqlalchemy import SQLAlchemy


def create_recipe(recipe_name, originator, directions):
    """Create and return a new recipe"""

    recipe = Recipes(recipe_name = recipe_name, 
                    originator = originator, 
                    directions = directions)

    db.session.add(recipe)
    db.session.commit()

    return recipe


def all_recipes():
    """Return all recipes"""

    return Recipes.query.all()


def alphabetical_recipes():
    """Return all recipes in alphabetical order"""

    q = Recipes.query

    return q.order_by('recipe_name')


def get_recipe_by_id(recipe_id):
    """Find recipe using id"""

    return Recipes.query.get(recipe_id)


def get_recipe_by_name(recipe_name):
    """Find recipe using recipe_name"""

    return Recipes.query.get(recipe_name)


def get_recipes_by_ingredient(ingredient_id):
    """Return all recipes that contain a specific ingredient"""
    
    ingred = get_ingredient_by_id(ingredient_id)
    recipes = alphabetical_recipes()
    rec_inc_ing = []    
    
    for recipe in recipes:
        if ingred in recipe.ingredients:
            rec_inc_ing.append(recipe)

    return rec_inc_ing



def create_ingredient(ingredient_name):
    """Create and return a new ingredient"""

    ingredient = Ingredients(ingredient_name = ingredient_name)

    db.session.add(ingredient)
    db.session.commit()

    return ingredient


def add_ingredient_to_recipe(ingredient_id, recipe_id):
    """Append ingredient to recipe ingredient list"""

    ingr = get_ingredient_by_id(ingredient_id)
    rec = get_recipe_by_id(recipe_id)

    rec.ingredients.append(ingr)

    db.session.add(rec)
    db.session.commit()


    return rec.ingredients 


def all_ingredients():
    """Return all ingredients"""

    return Ingredients.query.all() 


def alphabetical_ingredients():
    """Return all ingredients in alphabetical order""" 

    q = Ingredients.query
        
    return q.order_by('ingredient_name')
    

def get_ingredient_by_id(ingredient_id):
    """Find ingredient using id"""

    return Ingredients.query.get(ingredient_id)


def get_ingredient_by_name(ingredient_name):
    """Find ingredient using ingredient_name"""

    return Ingredients.query.filter(Ingredients.ingredient_name == ingredient_name).first()


def create_rating(recipe_id, rating):
    """Create and reutrn a new rating"""

    rating = Ratings(recipe_id = recipe_id, rating = rating)

    db.session.add(rating)
    db.session.commit()

    return rating


def create_note(recipe_id, note):
    """Create and return a new note"""

    note = Notes(recipe_id = recipe_id, note = note)

    db.session.add(note)
    db.session.commit()

    return note


def create_recipe_tag(tag_name):
    """Create and return a new recipe tag"""

    r_tag = Recipe_Tags(tag_name = tag_name)

    db.session.add(r_tag)
    db.session.commit()

    return r_tag


def all_tags():
    """Return all tags"""

    return Recipe_Tags.query.all() ##


def get_recipe_tag_by_id(tag_id):
    """Find recipe tag using id"""

    return Recipe_Tags.query.get(tag_id)


def get_recipe_tag_by_name(tag_name):
    """Find recipe tag using tag name"""

    return Recipe_Tags.query.filter(Recipe_Tags.tag_name == tag_name).first()


def add_tag_to_recipe(tag_id, recipe_id):
    """Add a tag to a recipe"""

    tag = get_recipe_tag_by_id(tag_id)
    rec = get_recipe_by_id(recipe_id)

    rec.tags.append(tag)

    db.session.add(rec)
    db.session.commit()

    return rec.tags






if __name__ == '__main__':
    from server import app
    connect_to_db(app)

