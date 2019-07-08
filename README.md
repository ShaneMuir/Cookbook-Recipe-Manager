# Recipe Manager | Cookbook App
## [Demo Here](https://milestone4.herokuapp.com/)
What is 'Recipe Manager | Cookbook' - It's an app built with Flask and MongoDB. In this application I use technology learnt on my coding journey to demonstrate how a document based database can be ultilise efficiently and effective to create simple yet effective scalable apps on the web. The aim of this project is to showcase my tech learnt so far from the course. 

Throughout this project I will make use of [Python](https://www.python.org/) a high end programming language along with [Flask](http://flask.pocoo.org/) a Python micro framework and [MongoDB](https://www.mongodb.com/) a document based database. 

With these tools I will be able to showcase all I have learnt from Code Institute so far, majority of my back-end logic will be written in Python running on the Flask framework using a document based database.

---
## UX
I wanted to created a seamless app for people to be able to easily store recipes.
The app is designed to allow for users to create, store and manage recipes seamlessly. 
I've developed the app in a way so that users data is protected by user restrictions where if you did not create the recipe then only the creator the recipe can edit that particular recipe or delete it from the database. Of course the site admin can over rule these restrictions but for all website user this is a level of protection for their stored recipes.
Within the application design I added a profile page this creates a simple way for the website user to quickly see all there stored recipes.
Lots of people may use cookbooks to refer from when cooking a meal, this app allows user to then store they're cookbook recipes into one place accessible and secure online. 

---
## User Stories
Reason's why Recipe Manager | Cookbook was created.
> As a user I need a place where I can collate and store recipes I like.

>There lots of recipes books out there but why can't I just store the recipes I like in one place.

>Lots of websites about for looking up a recipe but wouldn't it be simple to be able to store my own recipes somewhere.

>I need an app where I can store my recipe data and be have a page with all my listings in a view that is easily digestible. 

---
## Wireframes 
[Desktop View](https://raw.githubusercontent.com/ShaneMuir/Milestone-4/master/wireframes/Cookbook%20Desktop%20homepage.png)
[Tablet View](https://raw.githubusercontent.com/ShaneMuir/Milestone-4/master/wireframes/Cookbook%20Tablet%20homepage.png)
[Mobile View](https://raw.githubusercontent.com/ShaneMuir/Milestone-4/master/wireframes/Cookbook%20Mobile.png)

---
### Database Schema
In this project before starting on development I begin planning my database schema from how I wanted my database to work. Throughout the project design my schema has changed slightly but has given me good knowledge of how my database needed to be set out. 

See my database Schema [here.](#)

---
## Cookbooks Functionality
The app's main functionality is that it is capable of communicating to a dedicated document based database running on mLab using MongoDB. By using Python/Flask alongside Mongo I have been able to create an application that register and stores user data and recipe data. 

By allowing users to be able to register with an account in order to create and store recipes on the app this has allowed me to be able to restrict certain views and put user restrictions in place to protect user recipe data.

The app uses back-end logic where restrictions are used. This is to create a better user experience with creating and storing data and enables me to add a level of security to my app. 

My application is scalable and responsive meaning it will perform best on any device it's loaded on. 

Within in my applications functionality I create a search bar to allow users to search any recipe within my database straight from a input bar. Text is entered and based on the query provided the app will filter the database's collection. To expand further on the searching capability of my app is the ability to filter recipes by either diet label or health label. This functionality allows the user to easily filter the database based on a certain set of filters set. 

My website is capable of register and logging in users, this feature allows me to create user restrictions and view restrictions this enables me to add extra levels of security where needed to protect my database or user data. 

My app is capable of locking down user data and only users who created that recipe can edit or delete it.

---
## Technology Used
- [Python 3](https://www.python.org/download/releases/3.0/)
- [Flask 1.0.2](http://flask.pocoo.org/)
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CCS3/SCSS](https://sass-lang.com/)
- [Materialize](https://materializecss.com/)
- [JavaScript](https://www.javascript.com/)
- [jQuery](https://jquery.com/)
- [MongoDB](https://www.mongodb.com/)
- [mLab](https://mlab.com/)

---
## Database data

All my recipe data was source from [**Edam**](https://developer.edamam.com/edamam-recipe-api) a free recipe search API that can provide recipe data from calling a API endpoint and receiving the data back as [JSON](https://www.json.org/). The way I ultilise this API was by using Python requests and creating a simple but yet effective CLI (Command Line Interface) script which was taken and adapted from the course material. In the course we made a program to work with MongoDB via the CLI. By creating a script to request data from the API I then adapt the Mongo CLI program to then inject my retrieved data and insert it into a Mongo collection. My import script can be found within this repo.

---
### Things that could be improve if had more time
- Filters on index page could be made more dynamic so that if new diet labels or health labels that are not on the list could be populated too in the back-end.

- Reset password could be implemented for in case a user forgets their password.

- Logging vital system info and app info upon crashes or 404's, by this I mean we could find out what request.path they was on for 404's or for system error we could have the debug report be logged to a file and send to the site admin so that any system errors can be captured 

- AJAX functionality on the front-end.

##### Why I built 'Recipe Manager | Cookbook'

The main reasoning behind the project was inspired by Code Institute as the brief was to create a cookbook type project. But my main inspiration came from [Blue Apron](https://www.blueapron.com/cookbook). For days before embarking on development with my milestone I visited and navigated around a lot of recipe sites and tried looking for functionality that sites were lacking and put my main focus on this. I wanted to create something for users that wasn't already out there. For free. This project will be release under MIT and I will detail below within this document how you as a developer can get a copy or clone my app and expand on it or even make it your own. I will explain in detail how I used the tech and what I used to develop and deploy my app. 

---
## Testing
Most of the applications testing was done throughout development, most of which was manual tests. I will outline most of what I did below for documentation purposes.

**Testing Flask** - Within my settings I had flask's debugger set to 
```python
debug=True
```
This is so when Flask ever encounters a error the application knows to display this error in the view to give indication of what caused the app to crash.

I would work in small sprints where every step in my development I would ensure my app is still working as expected and where the app encounters any errors I would debug the source until rectification was a success. Where needed I would document the error and the remediation taken in case of future occurrences. 

Doing this meant after a while the error codes became more familiar to me. And from this debugging each error become less time consuming. 

---

**Testing Python** - When writing Python code I would normally write this is small chunks and do any routine testing from the CLI and where needed use the Python Interpreter to test any functions or statements. 

---

**Testing Flask Views** - In Flask each app's route uses a view template from my app structure these views were tested throughout every stage within my development process. Where needed I would test each view worked as expected when added new code or functionality to my app.

When passing any data down to the view I would firstly always ensure the data is there via using extra code within the back-end before sending down the data in the request. For example if I wanted to load my recipe collection in the back-end and send it to the view I would first ensure the data was loaded correctly by perform some back-end logic then pass this data to the view template whilst also checking the data was sent correctly to the front-end by perform the same back-end tests but on the front end before designing and displaying the mark up how I wanted it. 

---

**Testing the database** - Getting my data collections right was the trickiest part of this project. As through developing my application my database schema was constantly changing to the requirements of my app. Where multiple changes had to be made to the database in order for all my app's functionality to work properly.

When firstly create my recipes collection I made a Python program to pull data from a API and then insert this data is a data structure that was right for my databases schema. Doing this allowed me to expand on the Mongo CLI program we created through the course and use this within my applications development process. Below I will give examples of how the [import.py](https://github.com/ShaneMuir/Milestone-4/blob/master/import.py) script helped me in my project.

By creating my own Mongo import script I was able to effortlessly pull recipe data from an already available recipe API and then select the data I wanted and structure it in a way needed for my application.
```python
url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}&from=1&to=2"
search = "sushi"
api_id = "api_id_here"

api_key = "api_key_here"
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

}}
pprint(recipe)
```
Above is a snippet from my import program it shows from just a very few lines of code I was able to pull mass amounts of recipe data however I needed it. And by using Pythons [pprint](https://docs.python.org/3/library/pprint.html) module I was able to print these in a easily digestible way for me to know how this data was going to be injected into my database.

After ensuring the data was how I needed it I could then perform some checks before perform an insert into my Mongo database collection.
```python
i = input("Y/N: ")
if i == "Y":
coll = mongo.db.recipe
coll.insert_one(recipe)
```
This is how I collected my recipe data to play about with at the beginning of my app development in order to get the UPDATE, DELETE and READ methods working within my app. 

---

**Testing CRUD**

**READ**
Firstly before anything I wanted to make sure that I could display to my users the recipes I'd already collected and inserted into my db. To do this I had to create a home route and load the recipe collection within this route then pass the data to the view. As previously mentioned for the views I would constantly throughout the project development ensure there was no errors from Flask/Jinja before progressing with functionality of my app. 

In order to test that the recipe collection had successfully made it onto the app view I first assigned the data to a variable and tested within the Python interpreter that the data was loaded successful and could be printed to the terminal. After this I perform the same tests on the front-end once happy I begin to develop the home route for users to view all my recipes in my database in one single view.

After I made a route so that my users could view a single recipe alone. I took the functionality from the task_manager project we created and transferred it over to my app. 

**UPDATE**
After successfully displaying my recipes and being able to view a single recipe I moved onto then allowed for a recipe to be updated. At this stage I realised I needed to adapt my database schema slightly as I wanted to record who was editing or who created each recipe. I did this so further on in the project I could include some back-end logic to only allow for users who have created the recipe to be allowed to edit or delete that particular recipe. This was to ensure my database data was at least somewhat secure and users could not maliciously get there recipe data deleted. 

Testing the update recipes route was a case of trying the update_one method and applying this to a route that allowed a user to update the record based on some input by the user posting by the update recipe form. Upon a successful edit I would check in the single recipe view and by printing the entire recipe to the terminal that all user edited fields has updated.

**DELETE**
Testing the delete function in my app was a case of creating the route and then testing that route within the browser, I would grab a recipe ID and then enter the URL needed for that route to perform. After deleting a record I would flash a message for the user to be notified and also print a message to the terminal. To ensure the recipe was delete I would check in my view all recipes page along with checking the mLab website. 

**CREATE**
To test my create functionality of my app I would continuously fill out a recipe form and test that the route when posting create a new recipe within my recipe collection and that all the fields I needed were created successfully.

Once my CRUD functionality was in place I tested each form multiple times and tried to break each field or manipulate each form to perform unexpected. I have had my apps functionality tested multiple times by friends, family and everyone over at Slack who took the time out to try break my app. Where bugs were identified I made a note and fixed each issue.

From this I am confident that my CRUD functionality in my app is all working and without any bugs or errors being produced. In the case the app does crash or error there is measures in place to log the error, time/date, and user details and email this over to the admin for investigation.

---

**Authentication & Authorisation**
To allow for user restrictions and page restrictions in my app I needed to allow for user registration. Initially I just allowed for the User to register with a username and this would then be captured and inserted into my user collection against a user_id. 

After developing this functionality I wanted to improve it to allow for users to have passwords. This was due to how I made the user creation route, if a user entered a username already within my db I would notify the user of this and ask them to try another, it then become apparent that said user could ignore my notification and proceed to just login with the username they tried to register with as no password was needed for logging in. This was deemed a major data protection breech for my users so I went away and tho the project brief doesn't require user authentication with a password and it was not needed to restrict views or data, I added the functionality in anyway to better project my database and user data.

Password hashing was implemented using [werkzeug.security](https://werkzeug.palletsprojects.com/en/0.15.x/utils/#module-werkzeug.security) 

Now I was able to have peace of mind that my user recipe data was protected and could being with authorization of certain pages or recipes.

I was able to restrict certain views easily by added some back-end logic to perform a check and determine the outcome.
```python
if 'logged_in' not in session: #Check if its a logged in user
flash('Sorry, only logged in users can view the profile page. Please register')
return redirect(url_for('index'))
```
So the `logged_in` variable was created upon login/register of a user and if said user was not logged in or registered then this validation would fail and so redirect any user not logged in to the index with a notification message advises why.

Whereas if the user is logged in then the route would of work fine and the user would be able to go to the 'Profile_page'.

I was able to restrict users from being able to edit/delete other peoples records by added some extra back-end logic to my app to check whether the logged in user created the recipe or not. 
```python
if user['name'].title() == the_recipe['username'].title(): #If user created then user can edit or delete
```
and if the user was not the creator then they would be notified and returned back to the index.

In the views being able to restrict certain mark up was a case of using the Jinja template language with logic and applying restrictions around elements on the page. 
```python
{% if 'logged_in' in session %} {% if session['username'].title() == recipe.username.title() %}
{% else %}
{% endif %} {% endif %}
```
So here I was able to check if `logged_in` was in session and if so, if the username logged in matched the creator of that recipe then said user was able to view certain elements within my app.

---

**Responsiveness** - My app is fully responsive, through the entire development and design process I continuously tested my app under Chrome Developer tools and testing various different screens sizes. By this I was able to perform periodic checks throughout the development process to ensure that my app was responsive across all device screens ranging from extra small to extra large. Where needed I I just media queries to fix any resolution issues or responsiveness issues. I have built my app on the [Materialize CSS framework.](https://materializecss.com/) A modern responsive front-end framework based on Material Design but where custom design has been made I have added additional CSS within my own file to adding custom design to my app. 

My app has been testing by various student from the Slack community and by friends and family members where needed notes were made and identified bugs were fixed. 

From doing this I have been able to confidently say that my app is fully responsiveness across all devices. 

---

**Browser compatibility** 

My app does not work on IE, although I wanted to have my app backward compatible with all browsers I couldn't have it on IE due to Materialize and using elements that are not support by old Browsers.

My app will be fully functional across all major modern browsers. I have tested my app on the following browsers.

- [Chrome](https://www.google.com/chrome/)
- [Firefox](https://www.mozilla.org/en-GB/firefox/new/)
- [Opera](https://www.opera.com/)
- [IE Edge](https://www.microsoft.com/en-gb/windows/microsoft-edge)
- [Safari](https://support.apple.com/en_GB/downloads/safari)
- [Chrome Mobile](https://chrome.en.softonic.com/)

---

## Resource Sites Used
- [Edam](https://developer.edamam.com/edamam-docs-recipe-api)
- [Materialize Icons](https://materializecss.com/icons.html)
- [Unplsash](https://unsplash.com/)
- [Materialize Docs](https://materializecss.com/)
- [Flask Docs](http://flask.pocoo.org/docs/1.0/)
- [Mongo Docs](https://docs.mongodb.com/)
- [Slack](https://slack.com/intl/en-gb/)
- [Stack Overflow](https://stackoverflow.com/)
- [Google](https://google.com/)
- [YouTube](https://www.youtube.com/)

---

### HTML & CSS
All my HTML and CSS is valid, checked with the following validators

- [HTML Validator](https://validator.w3.org/)
-  [CSS Validator](https://jigsaw.w3.org/css-validator/)

#### Website Performance
Through the entirety of my project website performance is at the forefront of my mind. mark up has been optimized for website performance along with CSS/JS. All images have been compressed. As the project is on heroku the server can not be optimized.

---

## Deployment 
Getting my application ready for deployment consisted of the following:- 
1. Removing all my hard-coded environment variables to project my keys and secrets. These were placed in the .bashrc for development and entered into Heroku's Config Vars for production.
2. Ensuring the applications requirements.txt is up-to-date with all the latest packages installed for my app being noted on this file. 
	**The command to update requirements**
		```
		pip3 freeze > requirements.txt
		```
3. Set up the the Procfile - *A procfile is required by Heroku in order to tell the service worker what command to run for my application to start.*
4. Set Flask's debugging to False.
5. Push all my latest production ready code to GitHub ready for deployment via Heroku's GitHub function where you can deploy from GitHub the production ready app.

**Upon successful deployment Heroku will give you the URL that is hosted your app**

*Upon unsuccessful deployment Heroku will log the cause of the error and this is view able in the 'view log' section on the Heroku website. Here you will find a detailed report of what has cause your application not to be deployed successfully.*

### Expanding on my project

To get set up with a copy of my project you can do this multiple ways. 

**Via GitHub** -  
1. You can manually download locally to your machine and then upload to your preferred IDE. 
2. Install the projects requirements.txt using `pip3 install -r requirements.txt`
3. You will need to update a few enviroment varaiable before we can run the app.
	1. `app.config["MONGO_DBNAME"] =  "cookbook"`
	2. `app.config["MONGO_URI"] = os.getenv("MONGO_URI", "monogodb://localhost")`
	3. `app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")`
4. Once the above steps are complete you can try run the application using `python3 main.py`

**Via the CLI** -
1. Clone my repo via Git using the following command `https://github.com/ShaneMuir/Milestone-4.git`
2. Install the projects requirements.txt using `pip3 install -r requirements.txt`
3. You will need to update a few enviroment varaiable before we can run the app.
	1. `app.config["MONGO_DBNAME"] =  "cookbook"`
	2. `app.config["MONGO_URI"] = os.getenv("MONGO_URI", "monogodb://localhost")`
	3. `app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")`
4. Once the above steps are complete you can try run the application using `python3 main.py`

## Credits & Acknowledgments 
Credit is due to the following names. I would like to thank each and everyone who has helped or contributed to my project in any way. Please see list of names below:

- Mentor **Spencer Barriball**
- Youtuber **Pretty Printed**
- Slack Users **johnL3_alumni, RyanCooper, Seán, robinz_alumni, Sonya_alumni**
- Flask Megua Tutorial creator **Miguel Grinberg**
- Head First Python: A Brain-Friendly Guide **Paul Barry**

# LICENSE
This project is release under the **MIT** licence. For more info [here.](https://raw.githubusercontent.com/ShaneMuir/Milestone-4/master/LICENSE.md)