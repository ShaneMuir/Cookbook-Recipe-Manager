import os, env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "organic"
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'monogodb://localhost')

mongo = PyMongo(app)
    
@app.route('/')
@app.route('/get_recipes')
def home():
    return render_template('index.html', recipe=mongo.db.recipe.find())
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)