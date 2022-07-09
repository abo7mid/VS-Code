from flask import Flask, flash, redirect, render_template, request, session
import flask
from mysqlconnection import connectToMySQL # import the function that will return an instance of a connection


app = Flask(__name__)
app.secret_key = '#$%#@!!!'
@app.route("/",methods=['GET','POST'])
def index():
    is_valid = True
    mysql = connectToMySQL('mydb')
    if request.method == 'POST':
        if len(request.form['fname']) < 5:
            flash("firstname should be more than 5 chars")
            is_valid = False
        if len(request.form['lname']) < 5:
            flash("lastname should be more than 5 chars")
            is_valid = False
        if len(request.form['occup']) < 5:
            flash("occupation should be more than 5 chars")
            is_valid = False

        if not is_valid:
            return redirect('/')
        else:
            if not '_flashes' in session.keys(): # no flash messages means all validations passed
    	        # add user to database
                query = 'INSERT INTO friends (firstname,lastname,occup,created_at,updated_at) VALUES(%(fname)s, %(lname)s, %(occup)s,NOW(),NOW());'  # call the query_db function, pass in the query as a string
                # query = 'INSERT INTO friends (firstname,lastname,occup) VALUES(%(fname)s, %(lname)s, %(occup)s);'  # call the query_db function, pass in the query as a string
                data = {
                    "fname":request.form['fname'],
                    "lname":request.form['lname'],
                    "occup":request.form['occup'],
                }

                insert = mysql.query_db(query,data)
                flash("Friend added successfully!")
                return redirect('/')

    mysql = connectToMySQL('mydb')	# call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    
    return render_template("index.html",all_friends=friends)
            
if __name__ == "__main__":
    app.run(debug=True)

