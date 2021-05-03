"""Tests for Recipe App"""

from crud import (create_recipe, all_recipes, alphabetical_recipes, get_recipe_by_name, get_recipe_by_id, get_recipes_by_ingredient, get_recipes_by_tag, create_ingredient, add_ingredient_to_recipe, all_ingredients, alphabetical_ingredients, get_ingredient_by_id, get_ingredient_by_name, create_rating, create_note, create_recipe_tag, all_tags, alphabetical_tags, get_recipe_tag_by_id, get_recipe_tag_by_name, add_tag_to_recipe, get_recipes_by_multiple_ing, string_to_list, add_or_create_tag, add_or_create_ing, update_recipe, update_rating, update_note, update_recipe_ing, update_tags)
from model import connect_to_db, db
from flask import (Flask, session)
import server
import unittest



class RecipeAppTests(unittest.TestCase):
    """Tests for the app"""

    def setUp(self):
        """Code to run before each test"""

        self.client = server.app.test_client()
        server.app.config['TESTING'] = True
        connect_to_db(server.app) #"postgresql:///testdb")
        db.create_all()
        # example_data()


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
        self.assertIn(b"Click an ingredient name to see", result.data)


    def test_tag_list_page(self):
        """Tests to see if the tag list page can be reached"""

        result = self.client.get("/tags")
        self.assertIn(b"Click a tag to see", result.data)


    def test_create_recipe_page(self):
        """Tests to see if the page for new recipe creation can be reached"""

        result = self.client.get("/create_recipe")
        self.assertIn(b"separate tags with commas", result.data)

###########
    def test_search_page(self):
        """Tests to see if the search page can be reached"""

        result = self.client.get("/search_recipes")
        self.assertIn(b"Enter Ingredients You Want", result.data)
###########
    def test_search_results(self):
        """Tests to see if the search results appear properly"""

        client = server.app.test_client()
        result = client.get("search_for_recipes_with_ing", data = {"ingredients":"Chicken, Butter"}, follow_redirects = True)
        self.assertIn(b"Butter", result.data)
        self.assertIn(b"Chicken", result.data)
        self.assertIn(b"Search Results", result.data)


    def test_recipe_form_submission(self):
        """Test to see if submitting the create recipe form takes the user to the recipe details page"""

        client = server.app.test_client()
        result = client.post("/create_recipe", data = {"recipe_name":"Food Tester", "originator":"Tester1", "ingredients":"Testing Food, Food Testing, Tasty Test", "directions":"Taste test food. Yum.", "notes":"test notes", "tags":"tester, test food", "rating":"1"}, follow_redirects = True)
        self.assertIn(b"This is recipe #", result.data)
# #######

    # def test



    # def test_create_recipe():
    #     """Test that """

# Things to test:
# does it prevent form submission if user doesn't enter required field?
# 

#Test for 


if __name__ == "__main__":
    unittest.main()
