from flask import Blueprint,render_template, request, redirect, url_for
import json
import sys
from datetime import datetime
import os
import csv
import pandas as pd
import requests
import functions

main = Blueprint('main',__name__)#routename = main

<<<<<<< HEAD

# Specify the directory where the images will be saved
UPLOAD_FOLDER = 'static/images'
UPLOAD_FOLDER2 = 'static/files'
=======
>>>>>>> 7e494eea9a6fba7bc0d90ea5406adf1007b8050c

recipes = functions.load_recipes_from_json()




#homepage
@main.route('/', methods=['GET'])
def home():
    recipes = functions.load_recipes_from_json()
    #print(recipes, file=sys.stderr)
    return render_template('index.html',recipes = recipes)



#add recipe
@main.route('/addrecipe',methods=['GET','POST'])
def add_recipe():
<<<<<<< HEAD
    message = None
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        category = request.form['category']
        cuisine = request.form['cuisine']
        instructions = request.form['instructions'].split('.')
        ingredients = request.form['ingredients'].split(',')
        date_published = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        images = request.files['image']
        

        #validation
        if not name or not description or not category or not cuisine or not instructions or not ingredients or not images:
            message = "All fields are required!"
        elif any(recipe['name'] == name for recipe in recipes):
            message = 'Recipe already exists.'
        else:
             # Check if a file was uploaded
            if 'image' in request.files:
                image_file = request.files['image']
                if image_file:
                    # Save the image file to the specified directory
                    filename = image_file.filename
                    image_file.save(os.path.join(UPLOAD_FOLDER, filename))

            # Load the existing recipes from the JSON file
            with open('recipes.json', 'r') as file:
                existing_recipes = json.load(file)
            

            # Generate a unique ID for the new recipe
            new_recipe_id = len(existing_recipes) + 1
            # Create a new recipe object
            new_recipe = { 
                'id': new_recipe_id,  
                'name': name, 
                'description': description, 
                'category': category, 
                'cuisine': cuisine, 
                'instructions': instructions, 
                'ingredients': ingredients, 
                'date_published': date_published,
                'image':image_file.filename
            }
            # Add the new recipe to the existing recipes
            existing_recipes.append(new_recipe)
            # Write the updated recipes back to the JSON file
            with open('recipes.json', 'w') as file:
                json.dump(existing_recipes, file, indent=4)

            #return to homepage
=======
    message = functions.add_recipe_function('recipes.json')
 
    if message == 'Success':
        return redirect(url_for('main.home'))
    return render_template('add-recipe.html',message=message)
>>>>>>> 7e494eea9a6fba7bc0d90ea5406adf1007b8050c
        
            if new_recipe in existing_recipes:
                return redirect(url_for('main.home'))
            
    return render_template('add-recipe.html',message=message)

#view recipes
@main.route('/view/<int:id>',methods=['GET','POST','PUT'])
def view_recipe(id):
    recipe = functions.view_recipe(id)
    if recipe != "not found":
        #print(recipe, file=sys.stderr)
        
        return render_template('viewrecipes.html',recipes = recipe)



<<<<<<< HEAD
=======
#editrecipe
@main.route('/editrecipe/<int:id>', methods=['GET','POST'])
def edit_recipe(id):    
    recipe = functions.get_by_id(id)
    message = functions.edit_recipe_function(id,recipe,'recipes.json',functions.UPLOAD_FOLDER)
    return render_template('editrecipe.html',recipe=recipe,message=message)

#delete recipe
@main.route('/delete_recipe/<int:id>', methods=['POST'])
def delete_recipe(id):    
    functions.delete_recipe(id)
    return redirect(url_for('main.home'))

>>>>>>> 7e494eea9a6fba7bc0d90ea5406adf1007b8050c
#search recipe
@main.route('/search',methods=['GET'])
def search_recipe():
    query= request.args.get('search')
    search_recipes = functions.search_recipe_function(query,recipes)
    return render_template('search-results.html', query=query, recipes=search_recipes)

#import recipes
@main.route('/import', methods=['GET','POST'])
def import_recipe():
    if request.method == 'POST':
        if 'import' in request.files:
<<<<<<< HEAD
            csvFile = request.files['import']
            filename = csvFile.filename
            csvFile.save(os.path.join(UPLOAD_FOLDER2, filename))
            if filename.endswith('.xlsx'):
                # Handle XLSX file
                csvFile = 'static/files/importedRecipes.csv'
                convert_xlsx_to_csv('static/files/' + filename, csvFile)
            
            # Open a json writer, and use the json.dumps() function to dump data      
            with open('recipes.json', 'r') as jsonf:
                existingRecipes = json.load(jsonf)

            # Open a csv reader called DictReader
            with open(csvFile) as csvf:
                save_directory = 'static/images'             

                # Convert each row into a dictionary and add it to data
                csvReader = csv.DictReader(csvf)                    
                for rows in csvReader:                    
                    image_filename = rows['name'] + '.jpg'
                    
                    # Combine the save directory and image filename to create the save path
                    save_path = os.path.join(save_directory, image_filename)
                    
                    # Create the save directory if it doesn't exist
                    os.makedirs(save_directory, exist_ok=True)
                    download_image(rows['image'], save_path)
                    
                    # Generate a unique ID for the new recipe
                    rows['id'] = len(existingRecipes) + 1
                    rows['instructions'] = list(rows['instructions'].split(". "))
                    rows['instructions'] = [instruction + '.' if index != len(rows['instructions']) - 1 else instruction for index, instruction in enumerate(rows['instructions'])]
                    rows['ingredients'] = list(rows['ingredients'].split(', '))
                    rows['image'] = rows['name'] + '.jpg'
                    
                    # Add the new recipe to the existing recipes
                    existingRecipes.append(rows)

            # Write the updated recipes back to the JSON file
            with open('recipes.json', 'w') as jsonFile:
                jsonFile.write(json.dumps(existingRecipes, indent=4))
                
=======
            functions.import_recipe()                
>>>>>>> 7e494eea9a6fba7bc0d90ea5406adf1007b8050c
            return redirect(url_for('main.home'))
        return 'Invalid file'
    return render_template('importRecipes.html')

<<<<<<< HEAD


#editrecipe
@main.route('/editrecipe/<int:id>', methods=['GET','POST'])
def edit_recipe(id):
    recipe = get_by_id(id)

    if request.method == 'PUT':
        # Retrieve the updated recipe data from the form
        name = request.form['name']
        description = request.form['description']
        category = request.form['category']
        cuisine = request.form['cuisine']
        instructions = request.form['instructions']
        ingredients = request.form['ingredients']

        print(cuisine, file=sys.stderr)
        print(description, file=sys.stderr)


        with open('recipes.json', 'r') as file:
            existing_recipes = json.load(file)


        for recipe in existing_recipes:
            if recipe['id'] == id:
                # Update the recipe fields
                recipe['name'] = name
                recipe['description'] = description
                recipe['category'] = category
                recipe['cuisine'] = cuisine
                recipe['instructions'] = instructions
                recipe['ingredients'] = ingredients

                break

        # Save the updated recipes back to the JSON file
        with open('recipes.json', 'w') as file:
            json.dump(existing_recipes, file)

        print(existing_recipes, file=sys.stderr)

    return render_template('editrecipe.html',recipe=recipe)
=======
#export recipes
@main.route('/export', methods=['GET','POST'])
def export_recipes():
    response = functions.export_recipes()
    return response

@main.route('/rate/<int:id>',methods=['POST'])
def rate_recipe(id):
        # rating = request.form.get('rating')
        # tt = request.form.get('tt')
        # print(rating, file=sys.stderr)
        # print('id=',id, file=sys.stderr)

        functions.rating(id)
        return view_recipe(id)
>>>>>>> 7e494eea9a6fba7bc0d90ea5406adf1007b8050c
