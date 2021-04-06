"""Model for Recipe App"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Recipes(db.Model):
    """A recipe"""

    __tablename__ = 'recipes'

    recipe_id = db.Column(db.Integer, 
                            primary_key = True,
                            autoincrement = True,)
    recipe_name = db.Column(db.String, 
                            nullable = False, 
                            unique = True,)
    originator = db.Column(db.String, 
                            nullable = False, )
    directions = db.Column(db.Text, )

    def __repr__(self):
        """Show info about recipe"""
        return f'< The recipe is {self.recipe_name}, from the kitchen of {self.originator}>'


class Ratings(db.Model):
    """Recipe rating"""

    __tablename__ = 'rating'

    rating = db.Coloumn(db.Integer,
                        primary_key = True,)
    recipe_id = db.Column(db.Integer,
                        db.ForeignKey('recipes.recipe_id'), )


class Notes(db.Model):
    """Notes about a recipe"""

    __tablename__ = 'notes'

    note_id = db.Column(db.Integer, 
                        primary_key = True,
                        autoincrement = True, )
    recipe_id = db.Column(db.Integer,
                        db.ForeignKey('recipes.recipe_id'), )
    note = db.Column(db.Text, )


class Tag_Recipe_Relation(db.Model):
    """Relationship table for recipe tags and recipes"""

    __tablename__ = 'tag_recipe_relation'

    tr_relaton_id = db.Column(db.Integer,
                            primary_key = True,
                            autoincrement = True, )
    recipe_id = db.Column(db.Integer,
                            db.ForeignKey('recipes.recipe_id'), )
    r_tag_id = db.Column(db.Integer,
                            db.ForeignKey('recipe_tags.r_tag_id'), )

class Recipe_Tags(db.Model):
    """Tags to further identify recipes for the user"""

    __tablename__ = 'recipe_tags'

    r_tag_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True, )
    r_tag_name = db.Column(db.String,
                        unique = True, ) #not sure if tag should be unique, but probably


class Recipe_Ingredient_Relation(db.Model):
    """Relationship table for recipes and ingredients"""

    __tablename__ = 'recipe_ing_relate'

    ri_relation_id = db.Column(db.Integer,
                                primary_key = True,
                                autoincrement = True, )
    recipe_id = db.Column(db.Integer, 
                            db.ForeignKey('recipes.recipe_id'), )
    ingredient_id = db.Column(db.Integer,
                            db.ForeignKey('ingredients.ingredient_id'), )


class Ingredients(db.Model):
    """Ingredients used for recipes"""

    __tablename__ = 'ingredients'

    ingredient_id = db.Column(db.Integer,
                            primary_key = True,
                            autoicrement = True, )
    ingredient_name = db.Column(db.String,
                                unique = True, )  #again, not sure if this should be unique


class Tag_Ingredient_Relation(db.Model):
    """Relationship table for ingredient tags and ingredients"""

    __tablename__ = 'tag_ing_relate'

    ti_relation_id = db.Column(db.Integer,
                                primary_key = True,
                                autoincrement = True, )
    ingredient_id = db.Column(db.Integer,
                                db.ForeignKey('ingredients.ingredient_id'), )
    i_tag_id = db.Column(db.Integer,
                                db.ForeignKey('ingredient_tags.i_tag_id'), )


class Ingredient_Tags(db.Model):
    """Tags to further identify ingredients for the user"""

    i_tag_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True, )
    i_tag_name = db.Column(db.String, )
    
    

