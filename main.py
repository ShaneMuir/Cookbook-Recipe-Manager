import os, math, re
from flask import Flask, render_template, redirect, request, url_for, flash, session, jsonify, json
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from forms import LoginForm, RegistrationForm, RecipeForm
from pprint import pprint


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "cookbook"
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "monogodb://localhost")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)



@app.route('/')
@app.route('/get_recipes')
def index():
    """Route lets users see all recipes, logged_in users can use CRUD"""
    page_limit = 6 #Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipe.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    recipes = mongo.db.recipe.find().sort('_id', pymongo.ASCENDING).skip((current_page - 1)*page_limit).limit(page_limit)
    
    

    
    
    return render_template('index.html', recipe=recipes, title='Home', current_page=current_page, pages=pages)
    
@app.route('/recipe/<recipe_id>', methods=['GET','POST'])
def recipe(recipe_id):
    """Route for viewing a single recipe, logged_in users can use CRUD"""
    a_recipe =  mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    pprint(a_recipe)
    return render_template('recipe.html', recipe=a_recipe, title=a_recipe['recipe_name'])
    
@app.route('/i-made-it/<recipe_id>')
def i_made_it(recipe_id):
    """Function to increment i-made-it counter"""
    mongo.db.recipe.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'i-made-it': 1}}
    )
    return redirect(url_for('recipe', recipe_id=recipe_id))

@app.route('/search')
def search():
    """Route for search bar"""
    page_limit = 6 #Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    db_query = request.args['db_query']
    total = mongo.db.recipe.find({'$text': {'$search': db_query }})
    t_total = len([x for x in total])
    pages = range(1, int(math.ceil(t_total / page_limit)) + 1)
    
    results = mongo.db.recipe.find({'$text': {'$search': db_query }}).sort('_id', pymongo.ASCENDING).skip((current_page - 1)*page_limit).limit(page_limit)
    return render_template('search.html', results=results, pages=pages, current_page=current_page)


@app.route('/filtered_search', methods=['GET', 'POST'])
def filtered():
    """Logic for allowing filtering"""
    page_limit = 6 #Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipe.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    
    if request.method == "POST":
        for i in request.form:
            if i == "diet_labels":
                filter_items = []
                items = request.form.getlist('diet_labels') #get as a list []
                my_key = request.form # get as a multdict 
                for item in items: # iterate through the list
                    for i in my_key: #grab key_name
                        filter_items.append({i: item})
                print(filter_items) 

                results = mongo.db.recipe.find({'$and': filter_items })
                return render_template('filter.html', title="Filtered Seach", results=results)
            
            if i == "health_labels":
                filter_items = []
                items = request.form.getlist('health_labels') #get as a list []
                my_key = request.form # get as a multdict 
                for item in items: # iterate through the list
                    for i in my_key: #grab key_name
                        filter_items.append({i: item})
                print(filter_items) 

                results = mongo.db.recipe.find({'$and': filter_items })
                return render_template('filter.html', title="Filtered Seach", results=results)
                
    
    recipes = mongo.db.recipe.find().sort('_id', pymongo.ASCENDING).skip((current_page - 1)*page_limit).limit(page_limit)
    return render_template('index.html', recipe=recipes, title='Home', current_page=current_page, pages=pages)
    

    
@app.route('/create_recipe', methods=['GET', 'POST'])
def create_recipe():
    """Create a new recipe to db collection"""
    if 'logged_in' not in session: #Check if its a logged in user
        flash('Sorry, only logged in users can create recipes. Please register')
        return redirect(url_for('index'))
            
    form = RecipeForm(request.form)
    if form.validate_on_submit(): #Insert new recipe if form is submitted
        recipes = mongo.db.recipe
        recipes.insert_one({
        'recipe': request.form['recipe_name'],
        'recipe_name': request.form['recipe_name'],
        'recipe_image': request.form['recipe_image'],
        'serving_size': int(request.form['serving_size']),
        'diet_labels': request.form['diet_labels'],
        'health_labels': request.form['health_labels'],
        'ingredients': request.form['ingredients'],
        'calories': request.form['calories'],
        'cooking_time': request.form['cooking_time'],
        'i-made-it': int(0),
        'username': session['username'],
        'description': request.form['description'],
        'source': request.form['source'],
        'likes': {}
        })
        flash('Recipe Added!')
        return redirect(url_for('index'))
    return render_template('add_recipe.html', form=form)
    
@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """Function to edit seclect recipe"""
    if 'logged_in' not in session: #Check if its a logged in user
        flash('Sorry, only logged in users can create recipes. Please register')
        return redirect(url_for('index'))
    form = RecipeForm()
    the_recipe = mongo.db.recipe.find_one_or_404({'_id': ObjectId(recipe_id)})
    if request.method == 'GET':
        form = RecipeForm(data=the_recipe)
        return render_template('edit_recipe.html', recipe=the_recipe, form=form)
    if form.validate_on_submit():
        recipe = mongo.db.recipe
        recipe.update_one({
            '_id': ObjectId(recipe_id),
        }, {
            '$set': {
        'recipe': request.form['recipe_name'],
        'recipe_name': request.form['recipe_name'],
        'recipe_image': request.form['recipe_image'],
        'serving_size': int(request.form['serving_size']),
        'diet_labels': request.form['diet_labels'],
        'health_labels': request.form['health_labels'],
        'ingredients': request.form['ingredients'],
        'calories': request.form['calories'],
        'cooking_time': request.form['cooking_time'],
        'i-made-it': int(0),
        'username': session['username'],
        'description': request.form['description'],
        'source': request.form['source']
            }
        })
        flash('Recipe updated.')
        return redirect(url_for('index'))
    
    return render_template('edit_recipe.html', recipe=the_recipe, form=form)
    
@app.route('/delete/<recipe_id>')
def delete_recipe(recipe_id):
    """Function for deleting a select recipe"""
    recipe = mongo.db.recipe
    recipe.delete_one({
        '_id': ObjectId(recipe_id)
    })
    flash('Recipe deleted')
    return redirect(url_for('index'))
    

        
@app.route('/register', methods=['GET', 'POST'])
def register():
    """Function for handling the registration of users"""
    if 'logged_in' in session: #Check is user already logged in
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
            
        user = mongo.db.user
        dup_user = user.find_one({'name' : request.form['username'].title()})
            
        if dup_user is None:
            user.insert_one({'name' : request.form['username'].title()})
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect(url_for('index'))
        
        flash('Sorry, username already taken. Please try another.')
        return redirect(url_for('register'))
                
    return render_template('register.html', form=form, title="Register")
    
    
    
@app.route('/login', methods=['GET', 'POST'])
def user_login():
    """Function for handling the logging in of users"""
    if 'logged_in' in session: #Check is already logged in
        return redirect(url_for('index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = mongo.db.user
        logged_in_user = user.find_one({'name' : request.form['username'].title()})
        
        if logged_in_user is None:
            flash('Incorrect username, please try again')
            return redirect(url_for('user_login'))
        session['username'] = request.form['username']
        session['logged_in'] = True
        return redirect(url_for('index'))
   
    return render_template('login.html', form=form, title='Login')
    
    
@app.route('/logout')
def logout():
    """Logs the user out and redirects to home"""
    session.clear() # Kill session
    return redirect(url_for('index'))
                
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)