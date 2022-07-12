import re
from flask import Flask, flash, redirect, render_template, request, session

from mysqlconnection import connectToMySQL


app = Flask(__name__)
app.secret_key = "!@#$"
@app.route('/',methods=['GET','POST'])
def index():
	if 'userId' in session:
		return redirect('/success')
	if request.method == "POST":
		if request.form.get('register'):
			is_valid = True
			NAME_RE = re.compile(r'^[a-zA-Z+_-]+$') # allow only letters and _- chars
			if len(request.form['firstname']) < 3 or not NAME_RE.match(request.form['firstname']):
				is_valid = False
				flash("First Name should be more than 3 characters and only characters allowd!","danger")

			if len(request.form['lastname']) < 3 or not NAME_RE.match(request.form['lastname']):
				is_valid = False
				flash("Last Name should be more than 3 characters and only characters allowd!","danger")
			
			EMAIL_RE = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')  # what do _-r^\$ means in regex
			if not EMAIL_RE.match(request.form['email']):
				is_valid = False
				flash("invalid email address!","danger")
			
			mysql = connectToMySQL('mydb')
			email = "SELECT * FROM users WHERE email = %(email)s" 
			data = {
                    "email":request.form['email'],
			}
			unique = mysql.query_db(email,data)
			print('checking currnet email returns',unique)
			if unique: # the query will returns id of an exsisting row of an email, if it returns the id, email exists 
				flash("email already exists!","danger")


			#here code for email should be unique
			
			
			if not request.form['password'] or not request.form['confirm']:
				is_valid = False
				flash("Passwords & confirm should not be empty!","danger")
			
            #here code for password length should be at least 8 chars and at least 1 special chars 

			if request.form['password'] != request.form['confirm']:
				is_valid = False
				print('password',request.form['password'], "confirm",request.form['confirm'])
				flash("Passwords should matches!","danger")
			print('register')

			if not is_valid:
				return redirect('/')

			else:
				if not "_flashes" in session.keys():
					mysql = connectToMySQL('mydb')
					# Note: We will need to call on the connectToMySQL function every time we want to execute a query
					# because our connection closes as soon as the query finishes executing.
					query = "INSERT INTO users (firstname,lastname,email,password,created_at,updated_at) VALUES(%(fname)s,%(lname)s,%(email)s,%(password)s,NOW(), NOW())"
					data = {
						"fname":request.form['firstname'],
						"lname":request.form['lastname'],
						"email":request.form['email'],
						"password":request.form['password'],
					}
					user = mysql.query_db(query,data)
					print('user',user)
					session['userId'] = user
					if(user):
						flash("You have been registered successfully!","success")
						return redirect('/success')
					else:
						flash("unknown error!","danger")


		if request.form.get('login'):
			print('login')
			is_valid = True
			EMAIL_RE = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')  # what do _-r^\$ means in regex
			if not EMAIL_RE.match(request.form['email']):
				is_valid = False
				flash("invalid email address!","danger")

			mysql = connectToMySQL('mydb')
			query = "SELECT * FROM users WHERE email = %(email)s"
			data = {
				"email":request.form['email'],
			}
			user = mysql.query_db(query,data)
			print(user)
			if not user:
				is_valid = False
				if request.form['email']:
					flash("email is not found!","danger")


			if not is_valid:
				return redirect('/')
			
			else :
				if not "_flashes" in session.keys():

					mysql = connectToMySQL('mydb')
					query = "SELECT * FROM users WHERE email = %(email)s"
					data = {
						"email":request.form['email'],
					
					}
					user = mysql.query_db(query,data)
					if request.form['password'] == user[0]['password']:
						session['userId'] = user[0]['id']
						print('success')
						return redirect('/success')
					else:
						flash("invalid email or password","danger")

						

			

	return render_template('index.html')



@app.route('/success')
def success():
	if not 'userId' in session:
		return redirect('/')
	mysql = connectToMySQL('mydb')
	current_user = mysql.query_db(f"SELECT * FROM users where id = {session['userId']}")

	return render_template('success.html',user=current_user)

@app.route('/logout')
def logout():
	if "userId" in session:
		del session['userId']
		flash("You've been logged out","danger")
		return redirect('/')
	else:
		return redirect('/')





app.run(debug=True)
