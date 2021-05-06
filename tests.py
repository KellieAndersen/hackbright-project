"""Tests for Recipe App"""

from crud import (create_recipe, all_recipes, alphabetical_recipes, get_recipe_by_name, get_recipe_by_id, get_recipes_by_ingredient, get_recipes_by_tag, create_ingredient, add_ingredient_to_recipe, all_ingredients, alphabetical_ingredients, get_ingredient_by_id, get_ingredient_by_name, create_rating, create_note, create_recipe_tag, all_tags, alphabetical_tags, get_recipe_tag_by_id, get_recipe_tag_by_name, add_tag_to_recipe, get_recipes_by_multiple_ing, string_to_list, add_or_create_tag, add_or_create_ing, update_recipe, update_rating, update_note, update_recipe_ing, update_tags)
from model import connect_to_db, db
from flask import (Flask, session)
import server
import unittest
import json
import test_seed 


class RecipeAppIntegrationTests(unittest.TestCase):
    """Integration tests for the app"""

    def setUp(self):
        """Code to run before each test"""

        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

        connect_to_db(server.app)
        db.create_all()
        test_seed.create_test_data()
        


    def tearDown(self):
        """Code to run after each test"""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()

    
    def test_homepage(self):
        """Tests to see if homepage can be reached"""

        result = self.client.get("/")
        self.assertIn(b"Welcome", result.data)

    
    def test_recipe_list_page(self):
        """Tests to see if the recipe list page can be reached"""

        result = self.client.get("/recipes")
        self.assertIn(b"All Recipes", result.data)


    def test_ingredient_list_page(self):
        """Tests to see if the ingredient list page can be reached"""

        result = self.client.get("/ingredients")
        self.assertIn(b"Click an ingredient to see", result.data)


    def test_tag_list_page(self):
        """Tests to see if the tag list page can be reached"""

        result = self.client.get("/tags")
        self.assertIn(b"Click a tag to see", result.data)


    def test_create_recipe_page(self):
        """Tests to see if the page for new recipe creation can be reached"""

        result = self.client.get("/create_recipe")
        self.assertIn(b"separate tags with commas", result.data)


    def test_search_page(self):
        """Tests to see if the search page can be reached"""

        result = self.client.get("/search_recipes")
        self.assertIn(b"Enter Ingredients You Want", result.data)


    def test_recipe_form_submission(self):
        """Test to see if submitting the create recipe form takes the user to the recipe details page"""

        client = server.app.test_client()
        result = client.post("/create_recipe", data = {"recipe_name":"Food Tester", "originator":"Tester1", "ingredients":"Testing Food, Food Testing, Tasty Test", "directions":"Taste test food. Yum.", "notes":"test notes", "tags":"tester, test food", "rating":"1"}, follow_redirects = True)
        self.assertIn(b"This is recipe #", result.data)


    def test_recipe_edit_form_submission(self):
        """Test to see if submitting the edit recipe form takes the user to the recipe details page including edits"""

        client = server.app.test_client()
        result = client.post("/edit_recipe/2", data = {
            "recipe_name":"Grilled Cheese with Bacon", 
            "originator":"Lana", 
            "ingredients":"Bread, Cheese, Butter, Bacon, Tomato", 
            "directions":"Ingredients: 2 slices of bread, 3 slices of your favorite cheese, 2 Tbsp butter, mayo, several slices of cooked bacon based on preference     Directions: 1. Spread inside of bread slices with butter. Put slices of cheese and bacon between breaed pieces.   2. Spread mayo on the outside of bread slices.   3. Melt a pat of butter on a hot griddle. Put sandwich on hot griddle after butter melts and toast to a golden brown.   4. Flip sandwich and toast other side until golden brown and the cheese has melted.   5. Turn heat off and plate sandwich with desired side(s). Enjoy your sandwich.",
            "notes":"", 
            "tags":"lunch, hot food",
            "rating":"4"}, follow_redirects = True)
        self.assertIn(b"Tomato", result.data)
        self.assertNotIn(b"Mayo", result.data)


class RecipeAppUnitTests(unittest.TestCase):
    """Unit tests for the app"""
    
    def setUp(self):
        """Code run before each test"""

        self.client = server.app.test_client()
        server.app.config['TESTING'] = True


    def test_string_to_list(self):
        """tests to see that strings split on ' ,' """

        assert string_to_list("faith, hope, love") == ["faith", "hope", "love"]


    # def test


if __name__ == "__main__":
    unittest.main()
