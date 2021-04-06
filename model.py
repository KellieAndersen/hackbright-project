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
    tag_id = db.Column(db.Integer,
                            db.ForeignKey('recipe_tags.tag_id'), )

class Recipe_Tags(db.Model):
    """Tags to further identify recipes for the user"""

    __tablename__ = 'recipe_tags'

    tag_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True, )
    tag_name = db.Column(db.String,
                        unique = True, )


