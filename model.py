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
        return f'< The recipe is {self.recipe_name}, 
        from the kitchen of {self.originator}, recipe_id {self.recipe_id}>'


class Ratings(db.Model):
    """Recipe rating"""

    __tablename__ = 'rating'

    rating_id = db.Coloumn(db.Integer,
                        primary_key = True,
                        autoincrement = True, )
    rating = db.Column(db.Integer,)
    recipe_id = db.Column(db.Integer,
                        db.ForeignKey('recipes.recipe_id'), )

    def __repr__(self):
        return f'<recipe_id {self.recipe_id} has a rating of {rating}>'

    
class Notes(db.Model):
    """Notes about a recipe"""

    __tablename__ = 'notes'

    note_id = db.Column(db.Integer, 
                        primary_key = True,
                        autoincrement = True, )
    recipe_id = db.Column(db.Integer,
                        db.ForeignKey('recipes.recipe_id'), )
    note = db.Column(db.Text, )

    def __repr__(self):
        return f'<recipe id {self.recipe_id} has notes at note_id {self.note_id}: {self.notes}>'

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

    def __repr__(self):
        return f'<tag-recipe-relationship id {self.tr_relation_id} is related to 
        recipe_id {self.recipe_id} and recipe-tag id {self.r_tag_id}>'

class Recipe_Tags(db.Model):
    """Tags to further identify recipes for the user"""

    __tablename__ = 'recipe_tags'

    r_tag_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True, )
    r_tag_name = db.Column(db.String,
                        unique = True, ) #not sure if tag should be unique, but probably

    def __repr__(self):
        return f'<recipe-tag id {self.r_tag_id} is {self.r_tag_name}>'


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
    
    def __repr__(self):
        return f'<ingredient-recipe-relationship id {self.ri_relation_id} is related to 
        recipe_id {self.recipe_id} and ingredient id {self.ingredient_id}>'


class Ingredients(db.Model):
    """Ingredients used for recipes"""

    __tablename__ = 'ingredients'

    ingredient_id = db.Column(db.Integer,
                            primary_key = True,
                            autoicrement = True, )
    ingredient_name = db.Column(db.String,
                                unique = True, )  #again, not sure if this should be unique
    def __repr__(self):
        return f'<ingredient_id {self.ingredient_id} is {ingredient_name}>'


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
    
    def __repr__(self):
        return f'<tag-ingredient-relationship id {self.ti_relation_id} is
         relates to ingredient_id {self.ingredient_id} and ingredient-tag id {self.i_tag_id}>'


class Ingredient_Tags(db.Model):
    """Tags to further identify ingredients for the user"""

    i_tag_id = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True, )
    i_tag_name = db.Column(db.String, )

    def __repr__(self):
        return f'<ingredient tag id {i_tag_id} is {i_tag_name}>'
    


def connect_to_db(flask_app, db_uri='postgresql:///recipes', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    #connect_to_db(app, echo=False)
