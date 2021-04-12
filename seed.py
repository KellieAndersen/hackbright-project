"""Script to seed database."""

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

with open('recipes.json') as f:
    recipe_data = json.loads(f.read())

recipes_in_db = []
for recipe in recipe_data:
    recipe_name = recipe['recipe_name']
    originator = recipe['originator']
    directions = recipe['directions']

    db_recipe = crud.create_recipe(recipe_name, originator, directions)

## check if there is a note, if recipe[note]....
    if recipe['note']:
        n = recipe['note']
        note = crud.create_note(db_recipe.recipe_id, n)

    if recipe['rating']:
        rate = recipe['rating']
        rating = crud.create_rating(db_recipe.recipe_id, rate)

    # if recipe['tags']:
    #     tags = recipe['tags']
    #     for tag in tags:
    #         if tag not in crud.all_tags():
    #             t = crud.create_recipe_tag(tag)
    #             crud.add_tag_to_recipe(t.tag_id,db_recipe.recipe_id) ## 
    #         else:
    #             crud.add_tag_to_recipe(tag.tag_id,db_recipe.recipe_id)

    ingredients = recipe['ingredients']
    for ingredient in ingredients:
        if ingredient not in crud.get_all_ingr_by_name():
            ing = crud.create_ingredient(ingredient) ## if statement if ing already in list, skip create
            crud.add_ingredient_to_recipe(ing.ingredient_id, db_recipe.recipe_id) ##
        else:
            crud.add_ingredient_to_recipe(ingredient.ingredient_id, db_recipe.recipe_id)

    recipes_in_db.append(db_recipe)
 











    #  {
        # "recipe_name": "",
        # "originator": "",
        # "ingredients": [""],
        # "directions": "",
        # "tags":[""],
        # "rating": "",
        # "note": ""
    # }