"""Script to seed a test database"""

import os
import json
from random import choice, randint

import crud
import model
import server

os.system('dropdb recipes')
os.system('createdb recipes')

model.connect_to_db(server.app)
model.db.create_all()

def create_test_data():

    with open('test_recipes.json') as f:
        recipe_data = json.loads(f.read())

    recipes_in_db = []
    for recipe in recipe_data:
        recipe_name = recipe['recipe_name']
        originator = recipe['originator']
        directions = recipe['directions']

        db_recipe = crud.create_recipe(recipe_name, originator, directions)

        if recipe['note']:
            n = recipe['note']
            note = crud.create_note(db_recipe.recipe_id, n)

        if recipe['rating']:
            rate = recipe['rating']
            rating = crud.create_rating(db_recipe.recipe_id, rate)

        if recipe['tags']:
            tags = recipe['tags']
            for tag in tags:
                exist_tag = crud.get_recipe_tag_by_name(tag)
                if exist_tag:
                    crud.add_tag_to_recipe(exist_tag.tag_id,db_recipe.recipe_id) ## 
                else:
                    t = crud.create_recipe_tag(tag)
                    crud.add_tag_to_recipe(t.tag_id,db_recipe.recipe_id)


        ingredients = recipe['ingredients']
        for ingredient in ingredients:
            ingred = crud.get_ingredient_by_name(ingredient)
            if ingred:
                crud.add_ingredient_to_recipe(ingred.ingredient_id, db_recipe.recipe_id)
            else:
                ing = crud.create_ingredient(ingredient)
                crud.add_ingredient_to_recipe(ing.ingredient_id, db_recipe.recipe_id)  


        recipes_in_db.append(db_recipe)

    return recipes_in_db