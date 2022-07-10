from flask import Flask, flash, render_template, request, session,redirect
import re
from mysqlconnection import connectToMySQL


app = Flask(__name__)
app.secret_key = "!@#$"
@app.route('/',methods=['POST','GET'])
def index():
	is_valid = True
	if request.method == "POST":
		# create a regular expression object that we'll use later   

		# if not request.form['email']:
		# 	flash("email should not be empty!","danger")
		# 	is_valid = False

		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
		#if the type of the form input is email the browser will validate the email, but we do own the browser's code, it may change any time, we have to have our own back-end validation
		if not EMAIL_REGEX.match(request.form['email']):    # test whether a field matches the pattern
			flash("Invalid email address!","danger")
			is_valid = False
		
		if not is_valid:
			return redirect('/')
		

		else:
			if not "_flashes" in session.keys():

				mysql = connectToMySQL('mydb')
				query = "SELECT * FROM emails WHERE email = %(email)s"
				data = {
					"email":request.form['email'],
				}

				unique = mysql.query_db(query,data) # return empty if email not found
				# print("unique",unique)
				if not unique: # if email is not registered allow it to be registered 
					mysql = connectToMySQL('mydb')

					query = "INSERT INTO emails (email,created_at) VALUES(%(email)s,NOW())"

					data = {
						"email":request.form['email'],
					}
					mysql.query_db(query,data)
					flash("email submitted successfully!","success")
					return redirect('/success')
				else:
					flash("email already exists!","danger")


	return render_template('index.html')



@app.route('/success',methods =['GET'])
def success():
	mysql = connectToMySQL('mydb')
	emails = mysql.query_db("SELECT * FROM emails")

	return render_template('success.html',emails=emails)



@app.route('/destroy/<int:id>')

def destroy(id):
	mysql = connectToMySQL('mydb')
	mysql.query_db(f"DELETE FROM emails WHERE id = {id}")
	flash("Email deleted successfully!","success")
	return redirect('/success')

app.run(debug=True)
