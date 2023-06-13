# import unittest
# import json
# from flask import Flask

# class TestUnitRoutes(unittest.TestCase):
#     def setUp(self):
#         self.app = Flask(__name__)
#         self.app.register_blueprint(main)

#     def test_add_recipe(self):
#         with self.app.test_client() as client:
#             # Step 1: Load existing recipes
#             with open('recipes.json', 'r') as file:
#                 existing_recipes = json.load(file)

#             # Step 2: Add a new recipe
#             response = client.post('/addrecipe', data={
#                 'name': 'Test Recipe',
#                 'description': 'Test Description',
#                 'category': 'Test Category',
#                 'cuisine': 'Test Cuisine',
#                 'instructions': 'Test Instructions',
#                 'ingredients': 'Test Ingredients'
#             }, content_type='multipart/form-data', follow_redirects=True)

#             # Step 3: Load updated recipes
#             with open('recipes.json', 'r') as file:
#                 updated_recipes = json.load(file)

#             # Step 4: Check if the new recipe is present in the updated recipes
#             new_recipe = {
#                 'name': 'Test Recipe',
#                 'description': 'Test Description',
#                 'category': 'Test Category',
#                 'cuisine': 'Test Cuisine',
#                 'instructions': 'Test Instructions',
#                 'ingredients': 'Test Ingredients'
#             }
#             self.assertIn(new_recipe, updated_recipes)

# if __name__ == '__main__':
#     unittest.main()
