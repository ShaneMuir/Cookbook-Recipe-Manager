#Import the pymongo package
import pymongo
#Import Python os module
import os, requests
from pprint import pprint

#config vars
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "organic"
COLLECTION_NAME = "recipe"

#Function to connection to our DB
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print('Mongo is connected')
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print('Could not connect to MongoDB: %s') % e

#Asigning our conneciton to a var
conn = mongo_connect(MONGODB_URI)

#put it all together
coll = conn[DBS_NAME][COLLECTION_NAME]

url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}&from=1&to=2"
search = "sushi"
api_id = "0edc596e"
api_key = "2d2f813ed902380b9482bdd0ce4ec391"
    
r = requests.get(url.format(search,api_id,api_key)).json()
    
    
recipe = {
        'recipe': search,
        'recipe_name': r['hits'][0]['recipe']['label'],
        'recipe_image': r['hits'][0]['recipe']['image'],
        'serving_size': int(r['hits'][0]['recipe']['yield']),
        'diet_labels':r['hits'][0]['recipe']['dietLabels'],
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
i = input("Y/N: ")
if i == "Y":
    coll = mongo.db.recipe
    coll.insert_one(recipe)