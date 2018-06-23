
from flask import Flask, redirect, render_template, request, url_for
from server import app
from todo import *
from calculator import *
from blog import *
from accounts import *
from survey import *

import _pickle as cPickle

#Database is a dictionary, it is the same as an array
# Except you can instantly access the thing you want
# For example birthdays['Ryan'] = 18/05/98

#users = cPickle.load(open("database.pkl", "rb")) #loads the users from the database
users = [User("p", "1")] #list of user objects 

current_user = None #everytime a user is modified, we must "save all the users"
# we cant save one user due to our design (we are not using database)

#current_user.get_todo_items() = [ToDo objects]

# This is the home page

@app.route("/", methods=["GET", "POST"])
def login():
	global current_user #because the variable has been declared globally, we need to "global" the varibale in order to access it
	global users
	failed = False


	

	#if True: 
	if request.method == "POST":
		failed = True
		for user in users:
			if request.form['username'] == user.get_username() and request.form['password'] == user.get_password():
			#if "p" == user.get_username() and "1" == user.get_password():
				current_user = user
				return redirect( url_for('todosite'))

	return render_template("index.html", failed=failed)

@app.route("/logout", methods=["GET", "POST"])
def logout():
	global current_user
	current_user = None #current user will only equal to none only when user is logged out
	return redirect( url_for('login'))

@app.route("/todolist", methods=["GET", "POST"]) 
def todosite(): #for this url execute that function
	global current_user
	global users
	if current_user is None: #if logged out, and user tries to login, the application will redirect them to the login page
		return redirect( url_for('login'))  


	if request.method == "POST": #If a form has been submitted
		if request.form['submit'] == "Save": #if the name of the submit button is "Save"
			newitem = ToDo(request.form['name'], request.form['date'], 
				request.form['additional']) #passes in the arguments for the objects, and
				# constructs the object. assigns it to "newitem"
			current_user.get_todo_items().append(newitem) #appends the object to the list
			##current_user.get_todo_items() = [ToDo objects]

			
		elif request.form['submit'] == "Done?":
			for item in current_user.get_todo_items(): 
				if int(request.form['id']) == int(item.get_id()): #if the ID of the object being 
				#clicked on is equal to the ID submitted by the page
					item.mark_as_done() #marks the item as true, this eliminates it fromt he webpage.
					#all objects of the webpage are inherently false
					break
		elif request.form['submit'] == "More":

			#Redirect is a built in flask function
			# It redirects you to any url
			# Url_for is another function that will automatically construct
			# the url for you. You put in the name of the function corresponding
			# to the page, AND any other things you want to pass into the page.
			return redirect( url_for('todomore', passedInID=request.form['id']) )

		cPickle.dump(users, open("database.pkl" , "wb")) #dumps the list of users to the file

	return render_template("Todolist.html", todo_items=current_user.get_todo_items())

@app.route("/todolist/completed", methods=["GET", "POST"]) 
def todocompleted(): #for this url execute that function
	global current_user
	global users
	if current_user is None:
		return redirect( url_for('login'))

	if request.method == "POST": #If a form has been submitted
		if request.form['submit'] == "Save": #if the name of the submit button is "Save"
			newitem = ToDo(request.form['name'], request.form['date'], 
				request.form['additional']) #passes in the arguments for the objects, and
				# constructs the object. assigns it to "newitem"
			current_user.get_todo_items().append(newitem) #appends the object to the list
			##current_user.get_todo_items() = [ToDo objects]

			
		elif request.form['submit'] == "Delete?":
			for i in range(len(current_user.get_todo_items())): 
				if int(current_user.get_todo_items()[i].get_id()) == int(request.form['id']): #if the ID of the object being 
				#clicked on is equal to the ID submitted by the page
					del current_user.get_todo_items()[i]
					break

		cPickle.dump(users, open("database.pkl" , "wb")) #dumps the list of usrs to the file

	return render_template("TodoCompleted.html", todo_items=current_user.get_todo_items())

@app.route("/todolist/more/<passedInID>", methods=["GET", "POST"])
def todomore(passedInID): #input id
	global current_user
	global users
	if current_user is None:
		return redirect( url_for('login'))

	foundItem = None

	for item in current_user.get_todo_items():
		if int(passedInID) == int(item.get_id()):
			foundItem = item
			break

	return render_template("TodolistMore.html", item=foundItem)
	# ^displays the page, and passes the arguments into the page 
	#todolistmore.html is the name of the file
	#todo_items=current_user.get_todo_items()) passes the objects in the database to the webpage
	#todo_items is a name

@app.route("/calculator", methods=["GET", "POST"])
def calculatorsite():
	if current_user is None:
		return redirect( url_for('login'))
	if request.method == "POST":
		try:
			if request.form['submit'] == "Calculate Monthly Payment":
				calculator_obj = Calculator()
				value = calculator_obj.calculate_monthly_payment(int(request.form['loanAmount']), float(request.form['interestRate'])/100, int(request.form['years'])*12+int(request.form['months']))
				return render_template("calculator.html", months=None, value=round(value,2), GPA=None, error=False)
			elif request.form['submit'] == "Calculate Term":
				calculator_obj = Calculator()
				months = calculator_obj.calculate_term(int(request.form['loanAmount']), float(request.form['interestRate'])/12/100, int(request.form['extraMonthlyPayment']))
				return render_template("calculator.html", months=round(months,1), value=None, GPA=None, error=False)
			elif request.form['submit'] == "Calculate GPA":
				calculator_obj = Calculator() #instantiates the function
				GPA = 76786
				return render_template("calculator.html", months=None, value=None, GPA=GPA, error=False)
		except:
			return render_template("calculator.html", months=None, value=None, GPA=None, error=True)
#when trying out the formula, remove try catch to see if the formula actually works, otherwise it will catch all errors

	return render_template("calculator.html", months=None, value=None, GPA=None, error=False)

@app.route("/blog", methods=["GET", "POST"])
def blogsite():
	global current_user
	global users

	if request.method == "POST":
		if request.form['submit'] == "Save":
			newitem = BlogPost(request.form['title'], request.form['text'], 
				request.form['date'], request.form['author'])
			current_user.get_blog_posts().append(newitem)

		elif request.form['submit'] == "Delete":
			for i in range(len(current_user.get_blog_posts())): 
				if int(current_user.get_blog_posts()[i].get_id()) == int(request.form['id']): #if the ID of the object being 
				#clicked on is equal to the ID submitted by the page
					del current_user.get_blog_posts()[i]
					break

		elif request.form['submit'] == "Modify":
			return redirect( url_for('modify_blog', id=request.form['id'])) #redirect user to the page "/modifyblog" while also taking the id variable with it

		cPickle.dump(users, open("database.pkl" , "wb"))

	if current_user is None:
		return redirect( url_for('login'))

	return render_template("blog.html", blog_posts=current_user.get_blog_posts()) #the function blogsite passes all the blogs the user has currently written from the current user

@app.route("/modifyBlog/<id>", methods=["GET", "POST"])
def modify_blog(id):
	global current_user
	global users

	if current_user is None:
		return redirect( url_for('login'))

	if request.method == "POST":
		if request.form['submit'] == "Save":
			for item in current_user.get_blog_posts():
				if int(id) == int(item.get_id()):
					item.change_text(request.form['text'])
					item.change_date(request.form['date'])
					item.change_author(request.form['author'])
					item.change_title(request.form['title'])

		cPickle.dump(users, open("database.pkl" , "wb"))
		return redirect(url_for('blogsite'))

	foundItem = None
	for item in current_user.get_blog_posts():
		if int(id) == int(item.get_id()):
			foundItem = item
			break

	return render_template("blogModify.html", blog_post=foundItem)

@app.route("/canteenSurvey", methods=["GET", "POST"]) 
def canteenSurvey(): #for this url execute that function
	global current_user
	global users
#make availability a checkbox
	foods = [Food("Kebab and roll", "Middle Eastern", 4, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], ["No", "Doesn't Matter"]), 
	Food("Winter Soup", "Western", 4, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], ["No", "Doesn't Matter"]),
	Food("Honey Soy Chicken", "Western", 5, ["Wednesday"], ["No", "Doesn't Matter"]),
	Food("Meat Pie", "Western", 3, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], ["Yes", "No", "Doesn't Matter"]),
	Food("Sausage Roll", "Western", 3, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], ["No", "Doesn't Matter"])]


	if request.method == "POST":
		recommendations = []
		print(request.form.getlist('availability'))
		try:
			for food in foods:
				if request.form['cuisine'] == food.get_cuisine():
					if int(request.form['price']) <= food.get_price() + 2 and int(request.form['price']) >= food.get_price() - 2:
						for submitted_day in request.form.getlist('availability'):
							if submitted_day in food.get_availability():
								if request.form['spicy'] in food.get_spicy():
									recommendations.append(food)
									break

			return render_template("survey.html", recommendations=recommendations, error=False)
		except:
			return render_template("survey.html", recommendations=recommendations, error=True)
	return render_template("survey.html", error=False)
