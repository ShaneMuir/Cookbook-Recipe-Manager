import os
import requests
from pprint import pprint
import pymongo
import mongo

""" ENVIROMENT VARIABLES """
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "cookbook"
COLLECTION_NAME = "recipe"


def mongo_connect(url):
    """Function to make a connection to our DB"""
    try:
        conn = pymongo.MongoClient(url)
        print('Mongo is connected')
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print('Could not connect to MongoDB: %s') % e

conn = mongo_connect(MONGODB_URI)  # Assign our connection to a var
coll = conn[DBS_NAME][COLLECTION_NAME]  # Put it all together

url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}&from=1&to=2"
search = "sushi"  # Name of the recipe
api_id = "0edc596e"
api_key = "2d2f813ed902380b9482bdd0ce4ec391"

r = requests.get(url.format(search, api_id, api_key)).json()  # Make a request

recipe = {
        'recipe': search,
        'recipe_name': r['hits'][0]['recipe']['label'],
        'recipe_image': r['hits'][0]['recipe']['image'],
        'serving_size': int(r['hits'][0]['recipe']['yield']),
        'diet_labels': r['hits'][0]['recipe']['dietLabels'],
        'health_labels': r['hits'][0]['recipe']['healthLabels'],
        'ingredients': r['hits'][0]['recipe']['ingredientLines'],
        'ingredients_raw': r['hits'][0]['recipe']['ingredients'],
        'calories': int(r['hits'][0]['recipe']['calories']),
        'cooking_time': r['hits'][0]['recipe']['totalTime'],
        'total_nutrients': r['hits'][0]['recipe']['totalNutrients'],
        'likes': {
        }
    }

pprint(recipe)

i = input("Y/N: ")  # If data is ok then populate theour DB
if i == "Y":
    coll = mongo.db.recipe
    coll.insert_one(recipe)
