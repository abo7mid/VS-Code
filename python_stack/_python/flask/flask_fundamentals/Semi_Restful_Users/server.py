from flask import Flask, flash, redirect, render_template, request, session

from mysqlconnection import connectToMySQL
# from mysqlconnection import MySQLConnection


app = Flask(__name__)

app.secret_key = "!@#$"

@app.route('/')
def root():
	return redirect('/users')


@app.route('/users')
def index():
	mysql = connectToMySQL("mydb")
	users=mysql.query_db("SELECT * FROM user")
	print(users)
	return render_template('index.html',users=users)





@app.route('/users/new',methods=['GET','POST'])
def create():
	if request.method == "POST":
		mysql = connectToMySQL('mydb')

		is_valid = True
		if len(request.form['fname']) <5:
			is_valid = False
			flash("First Name should be more than 5 characters")
		if len(request.form['lname']) <5:
			is_valid = False
			flash("Last Name should be more than 5 characters")
		if len(request.form['email']) <5:
			is_valid = False
			flash("Email should be more than 5 characters")

		if not is_valid:
			redirect('/users/new')
		else:
			if not '_flashes' in session.keys():
				query = "INSERT INTO user (firstname,lastname,email,created_at,updated_at) VALUES(%(fname)s,%(lname)s,%(email)s,NOW(),NOW())"
				data = {
					"fname":request.form['fname'],
					"lname":request.form['lname'],
					"email":request.form['email'],
				}
				result = mysql.query_db(query,data) # will return id of the new row ,record
				flash("user added successfully!")
				return redirect(f'/users/{result}')
	return render_template('create.html')





@app.route('/users/<int:id>')
def show(id):
	# id = int(id)
	mysql = connectToMySQL('mydb')
    
	query = "SELECT * FROM user WHERE id = %(id)s"
	
	data = {
		"id":id,
	}
	user=mysql.query_db(query,data)
	print(user)
	return render_template('show.html',user=user)






@app.route('/users/<int:id>/edit',methods=['GET','POST'])
def edit(id):
	# id = int(id)
	if request.method == "POST":
		print('POST')
		is_valid = True
		if len(request.form['efname']) < 4:
			is_valid = False
			flash("First Name should be more than 4 characters")
			print("First Name should be more than 4 characters")
		if len(request.form['elname']) < 4:
			is_valid = False
			flash("Last Name should be more than 4 characters")
			print("Last Name should be more than 4 characters")
		if len(request.form['eemail']) < 4:
			is_valid = False
			flash("Email should be more than 4 characters")
			print("Email should be more than 4 characters")
		
		
		if not is_valid:
			print('redirected')
			# return redirect(f'/users/{id}/edit')
		else:
			print("else")
			if not '_flashes' in session.keys():
				print('no errors')
				mysql = connectToMySQL('mydb')

				query = "UPDATE user SET firstname = %(fname)s, lastname = %(lname)s, email = %(email)s WHERE id = %(id)s"
				data = {
						"fname":request.form['efname'],
						"lname":request.form['elname'],
						"email":request.form['eemail'],
						"id":int(id),
				}
				mysql.query_db(query,data)
				flash('user updated successfully!')
				return redirect(f'/users/{id}')


	print('GET')
	mysql = connectToMySQL('mydb')
    
	query = "SELECT * FROM user WHERE id = %(id)s"
	
	data = {
		"id":id,
	}
	user=mysql.query_db(query,data)
	return render_template('edit.html',user=user)






@app.route('/users/<int:id>/destroy')
def delete(id):
	mysql = connectToMySQL('mydb')
	query = f"DELETE FROM user WHERE id={id}"
	mysql.query_db(query)


	return redirect('/users')

	
app.run(debug=True)




