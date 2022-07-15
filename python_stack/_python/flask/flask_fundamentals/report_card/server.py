from flask import Flask, flash, redirect, render_template, request, session, url_for

from mysqlconnection import connectToMySQL


app = Flask(__name__)
app.secret_key = "!@#$"


@app.route('/')
def index():
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    mysql = connectToMySQL('mydb')
    query = "SELECT * FROM Students"
    students = mysql.query_db(query)
    return render_template('index.html', students=students)


@app.route('/addstudent', methods=['POST', 'GET'])
def addstudent():

    if request.method == 'POST':
        is_valid = True

        if not request.form['firstname']:
            flash('First Name is required field', 'danger')
            is_valid = False

        if not request.form['lastname']:
            flash('Last Name is required field', 'danger')
            is_valid = False

        if not request.form['year']:
            flash('Year is required field', 'danger')
            is_valid = False

        if not is_valid:
            return redirect('/addstudent')

        else:
            if not '_flashes' in session.keys():
                mysql = connectToMySQL('mydb')
                query = "INSERT INTO Students (firstname,lastname,year,created_at,updated_at) VALUES(%(fname)s,%(lname)s,%(year)s,NOW(),NOW())"
                data = {
                    "fname": request.form['firstname'],
                    "lname": request.form['lastname'],
                    "year": request.form['year'],
                }

                result = mysql.query_db(query, data)
                if result:
                    flash("Student's been added successfully!", "success")
                else:
                    flash("Unknown Error", "danger")

    return render_template('addstudent.html')


@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
	if request.method == "POST":
		is_valid = True
		if not request.form['course']:
			flash("Course is required field", "danger")
			is_valid = False
		if not request.form['grade']:
			flash("Grade is required field", "danger")
			is_valid = False
		if not request.form['comment']:
			flash("Comment is required field", "danger")
			is_valid = False

		if not is_valid:
			return redirect(url_for('edit', id=id))

		else:
			if not "_flashes" in session.keys():
				mysql = connectToMySQL('mydb')
				query = "INSERT INTO Grades (course,grade,comment,Student_id,created_at,updated_at) VALUES(%(course)s,%(grade)s,%(comment)s,%(id)s,NOW(),NOW())"
				data = {
					"course": request.form['course'],
						"grade": request.form['grade'],
						"comment": request.form['comment'],
						"id": id,
				}
				grade = mysql.query_db(query,data)
				if grade:
					flash("grade accredited successfully!","success")
				else:
					flash("Unknown Error!","danger")
	return render_template('addGrade.html',id=id)


@app.route('/<int:id>')
def view(id):
	mysql1 = connectToMySQL('mydb')
	mysql2 = connectToMySQL('mydb')



	queryGrade = "SELECT * FROM Grades WHERE Student_id = %(id)s"
	queryFullName = "SELECT firstname,lastname FROM Students WHERE id = %(id)s"
	data = {
        "id": id
    }
	grades = mysql1.query_db(queryGrade, data)
	FullName = mysql2.query_db(queryFullName, data)
	if not grades:
		flash("the user does not have a card yet","danger")
		return redirect('/dashboard')
	# print(grades)
	# print(grades[0]['course'])
	return render_template('viewCard.html', grades=grades,fullname=FullName)


app.run(debug=True)



# NINJA BONUS: Allow the teacher to edit a grade

# NINJA BONUS: Allow the teacher to delete a grade

# SENSEI BONUS: Sort the grades on the report card from best to worst