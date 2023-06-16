from io import BytesIO
import unittest
from flask import Flask
import sys
import json
import os

sys.path.append("../SystemDeploymentProject")

import functions

class test_unit_routes(unittest.TestCase):
    
    def setUp(self):
        # Create a Flask test client
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True

<<<<<<< HEAD
        with app.test_request_context('/addrecipe', method='POST', data={
            'name': 'Test 1',
            'description': 'Test',
            'category': 'Test',
            'cuisine': 'Test',
            'instructions': 'Test',
            'ingredients': '1, 2',
            'image': (BytesIO(b'TestImage'), 'test.jpg')
        }):
            response = add_recipe()
            self.assertEqual(response.status_code, 302)
=======
>>>>>>> 7e494eea9a6fba7bc0d90ea5406adf1007b8050c
           
    def test_add_recipe_success(self):
        data = {
            'name': 'Test Recipe',
            'description': 'Test description',
            'category': 'Test category',
            'cuisine': 'Test cuisine',
            'instructions': 'Step 1. Test instruction',
            'ingredients': 'Ingredient 1, Ingredient 2',
            'image': (BytesIO(b'TestImage'), 'test.jpg')
        }
        with self.app.test_request_context('/addrecipe', method='POST', data=data, content_type='multipart/form-data'):
            # Call the add_recipe_function()
            result = functions.add_recipe_function('test_recipe.json')
            # Assert the expected result
            self.assertEqual(result, 'Success')

    def test_create_recipe_missing_fields(self):
        data2 = {
            'name': 'Test Recipe',
            'description': 'Test description',
            'category': 'Test category',
            'cuisine': '',
            'instructions': 'Step 1. Test instruction',
            'ingredients': 'Ingredient 1, Ingredient 2',
            'image': (BytesIO(b'TestImage'), 'test.jpg')
        }
        
        with self.app.test_request_context('/addrecipe', method='POST', data=data2, content_type='multipart/form-data'):
            result = functions.add_recipe_function('test_recipe.json')
            self.assertEqual(result, 'All fields are required!')

  #search recipe testing
    def test_search_recipe(self):
            # request query
            query = 'butter chicken'

            with open('test_recipe.json', 'r') as file:
                recipedata = json.load(file)
            
            with self.app.test_request_context('/search', method='GET'):
                # Call the add_recipe_function()
                result_query, result_recipes = functions.search_recipe_function(query,recipedata)
                # Assert the expected result
                self.assertEqual(result_query, query)
                self.assertEqual(len(result_recipes), 1)
                self.assertEqual(result_recipes[0]['name'], 'Butter Chicken')

    def test_search_recipe_no_results(self):
        # Set up request query
        query = 'salad'
        with open('test_recipe.json', 'r') as file:
                recipedata = json.load(file)
        with self.app.test_request_context('/search', method='GET'):
        # Call the search_recipe function
            result_query, result_recipes =  functions.search_recipe_function(query, recipedata)
            # Assertions
            self.assertEqual(result_query, query)
            self.assertEqual(len(result_recipes), 0)

    #edit recipe 
    def test_edit_recipe_success(self):
            # with open('test_recipe.json', 'r') as file:
            #     recipes = json.load(file)
            TEST_UPLOAD_FOLDER = 'test_images'

            data = {
                'name': 'Blueberry Pancake',
                'description': 'Delicious blueberry pancakes recipe',
                'category': 'Breakfast',
                'cuisine': 'American',
                'instructions': 'Step 1. Step 2. Step 3.',
                'ingredients': 'flour, milk, eggs, blueberries',
                'image': (BytesIO(b'TestImage'), 'test_pancake.jpeg')
            }
            with self.app.test_request_context('/editrecipe/1',method='POST', data=data, content_type='multipart/form-data'):
                # Call the add_recipe_function()
                result = functions.edit_recipe_function(1,data,'test_recipe.json',TEST_UPLOAD_FOLDER)
                # Assert the expected result
                self.assertEqual(result, 'Updated Successfully')



if __name__ == '__main__':
    unittest.main()