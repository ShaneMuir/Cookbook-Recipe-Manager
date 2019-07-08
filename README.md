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
### Wireframes 
[Desktop View](https://raw.githubusercontent.com/ShaneMuir/Milestone-4/master/wireframes/Cookbook%20Desktop%20homepage.png)
[Tablet View](https://raw.githubusercontent.com/ShaneMuir/Milestone-4/master/wireframes/Cookbook%20Tablet%20homepage.png)
[Mobile View](https://raw.githubusercontent.com/ShaneMuir/Milestone-4/master/wireframes/Cookbook%20Mobile.png)

---
### Database Schema
In this project before starting on development I begin planning my database schema from how I wanted my database to work. Throughout the project design my scehma has changed slightly but has given me good knowledge of how my database needed to be set out. 

See my database Schema [here.](#)

---
### Cookbooks Functionality
The app's main functionality is that it is capable of communicating to a dedicated document based database running on mLab using MongoDB. By using Python/Flask alongside Mongo I have been able to create an application that register and stores user data and recipe data. 

By allowing users to be able to register with an account in order to create and store recipes on the app this has allowed me to be able to restrict certain views and put user restrictions in place to protect user recipe data.

The app uses back-end logic where restrictions are used. This is to create a better user experience with creating and storing data and enables me to add a level of security to my app. 

My application is scalable and responsive meaning it will perform best on any device it's loaded on. 

Within in my applications functionality I create a search bar to allow users to search any recipe within my database straight from a input bar. Text is entered and based on the query provided the app will filter the database's collection. To expand further on the searching capability of my app is the ability to filter recipes by either diet label or health label. This functionality allows the user to easily filter the database based on a certain set of filters set. 

My website is capable of register and logging in users, this feature allows me to create user restrictions and view restrictions this enables me to add extra levels of security where needed to protect my database or user data. 

My app is capable of locking down user data and only users who created that recipe can edit or delete it.

---
### Technology Used
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
#### Database data

All my recipe data was source from [**Edam**](https://developer.edamam.com/edamam-recipe-api) a free recipe search API that can provide recipe data from calling a API endpoint and recieving the data back as [JSON](https://www.json.org/). The way I ultilise this API was by using Python requests and creating a simple but yet effective CLI (Command Line Interface) script which was taken and adapted from the course material. In the course we made a program to work with MongoDB via the CLI. By creating a script to request data from the API I then adapt the Mongo CLI program to then inject my retrieved data and insert it into a Mongo collection. My import script can be found within this repo.

---
### Things that could be improve if had more time
- Filters on index page could be made more dynamic so that if new diet labels or health labels that are not on the list could be populated too in the back-end.

- Reset password could be implemented for in case a user forgets their password.

- Logging vital system info and app info upon crashes or 404's, by this I mean we could find out what request.path they was on for 404's or for system error we could have the debug report be logged to a file and send to the site admin so that any system errors can be captured 

- AJAX functionality on the front-end.

##### Why I built 'Recipe Manager | Cookbook'

The main reasoning behind the project was inspired by Code Institute as the brief was to create a cookbook type project. But my main inspiration came from [Blue Apron](https://www.blueapron.com/cookbook). For days before embarking on development with my milestone I visited and navigated around alot of recipe sites and tried looking for functionality that sites were lacking and put my main focus on this. I wanted to create something for users that wasn't already out there. For free. This project will be release under MIT and I will detail below within this document how you as a developer can get a copy or clone my app and expand on it or even make it your own. I will explain in detail how I used the tech and what I used to develop and deploy my app. 
