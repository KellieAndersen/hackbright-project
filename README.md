# Recipe Rabbit

![rr_logo](/static/recipe_rabbit_logo.png)

Recipe Rabbit is a fullstack web application that is more than just another recipe app. Recipe Rabbit allows users to create and store recipes, edit recipes, tag recipes, and look up stored recipes in a vareity of ways. Recipes can be looked up by tag, recipe name, single ingredient, or using multiple ingredients. Don't just use any recipe, *cook it your way*.

### Technologies

- Python
- Flask
- SQLAlchemy
- PostgreSQL
- HTML/CSS
- Bootstrap
- JSON
- Jinja2

Dependencies can be found in requirements.txt.

### How to Use Recipe Rabbit

#### Homepage
Upon opening the app, the homepage will be shown. On the homepage, there are five options of things a user can do. These same options are also on the navigation bar which is present on every page.

![homepage](/static/rr_homepage.png)

#### View All Recipes
The first option is "View All Saved Recipes". When this is clicked, it will pull up a list of all the recipes that are already stored in the app in alphabetical order. 

![all_recipes](/static/rr_all_recipes.png)

#### Recipe Details
Each recipe name is a link to the details page for that recipe. This page contains all the information about the recipe including the recipe name, the ingredients, a directions section, any notes about the recipe, a rating on a scale of one to five, an originator (i.e. "From the Kitchen of:"...), and any tags associated with the recipe.
At the bottom of this page is an edit button. More about the edit function can be found further on in the document.

![recipe_details](/static/rr_recipe_details.png)

#### View All Ingredients
The second option is "View All Ingredients". This will pull up a list of all the ingredients currently used in any of the recipes stored in alphabetical order.

![all_ingredients](/static/rr_all_ingredients.png)

#### Recipes Including a Particular Ingredient
Each ingredient name is a link. When clicked, these will bring up a list of all recipes including that particular ingredient in alphabetical order. Each recipe name is also a link back to the recipe's details page.

![one_ing_recipes](/static/rr_one_ing.png)

#### View All Tags
The next option is "View All Tags". This option shows a list of all tags associated with any of the recipes in alphabetical order. Each tag name is a link.

![all_tags](/static/rr_all_tags.png)

#### Recipes Associated with a Particular Tag
Clicking on a tag name will bring up a list of all recipes associated with that tag in alphabetical order. Each of these recipe names is also a link to the recipe's details page.

![one_tag](/static/rr_with_tag.png)


#### Create a New Recipe
The fourth option on the home page is "Create a New Recipe". Clicking on this option takes the user to the recipe creation form.

![create_recipe](/static/rr_create_recipe.png)

The page instructs users on what input formats to give each section and some example text is given in each box so the user has a clear picture of what is required. Recipe Name, From the Kitchen of, Ingredient Names, and Directions are all required fields. Notes, Tag(s), and Rating are optional. Any field except for the rating field (which must contain a number from one to five) can be populated with anything the user wants. An ingredient or tag does not need to already be in the database for the user to use it. Any non-existent tag or ingredient will be created once the form is submitted.

![filled_create_form](/static/rr_create_filled.png)

Clicking the submit button at the bottom of the form creates the recipe using the inputs from the user and redirects the user to the new recipe's details page.

![new_recipe](/static/salmon_recipe.png)

#### Editing a Recipe
At the bottom of a recipe's details page there is an "Edit Recipe" button. Clicking this will redirect the user to an edit form for that recipe with current information pre-populated. Users can edit any and every part of the recipe as desired. Adding notes is a common use.

*Note: It is important that the ingredients and tags information lists do not end in a comma as this will cause the creation of a new empty tag or ingredient that will always show up in the All Ingredients or All Tags pages even if it is later removed from the recipe.*

![edit_form](/static/rr_edit.png)

If the edit button was clicked by accident, there is a back button at the top left of the page right under the navigation bar. This will take the user back to the details page that they were viewing before.
Clicking submit at the bottom of the edit form will alter the recipe according to any changes made by the user and redirect the user to the updated recipe details page.

![edited_recipe](/static/salmon_edited.png)

#### Search for Recipes
The final option on the homepage is "Search for Recipes: Ingredients Based Search". Selecting this option will bring up a search form.

![search_form](/static/rr_search.png) 

This form can take any ingredient name already included in the All Ingredients list, separated by commas. The purpose for this search is to find recipes that contain ingredients the user inputs. This might be useful if a user wants to know what recipes they can make with ingedients they have on hand.

![filled_search_form](/static/search_filled.png)

Once the form is submitted, the app will redirect to a list of recipes that contain *any* of the specified ingredients. Under each recipe is a list of all the ingredients used for that recipe, not just matched ingredients. This way, the user knows right away if it's a recipe that contains ingredients that the user doesn't have and can move on. Each recipe name is a link to that recipe's details page.

![search_results](/static/rr_search_results.png) 



### Future Version Planning

In future versions of this application, the following features will be implemented:

###### Log-In Function

A user would have to log in to their account to use the features on the site and have a separate account specific to them.

###### More Specific Search Results

When a user searches for recipes using multiple ingredients, the resulting list should be in order of how many ingredients match the input and those matching ingredients should be bolded in the ingredients list below the recipe name.

###### More Search Options

A search should also be able to look recipes up based on any or all of the following:
- Ingredients
- Tags
- Originators
- Ratings

The search also should allow the user to specify attributes that they do not want in the results (e.g. no beef, no recipes from Mom, no tags about birthdays, etc).

###### Better Layout for Recipe Details Page

The layout should separate the Ingredients from the Directions and should only list ingredients with their measurements.

###### Better Create Recipe Form (and, by default, better edit recipe form)

The form should be able to take in ingredients with their measurements instead of needing two different areas for ingredient names and ingredients with their measurements. The app should be able to separate out the measurements for ingredient table row creation.

The capitilization of certain recipe attributes, such as tags or ingredients, should not matter. More backend functions need to be able to deal with that.

###### Add Pictures

The user should be able to add pictures of their recipes and those should be visible at least on the recipe details page.

