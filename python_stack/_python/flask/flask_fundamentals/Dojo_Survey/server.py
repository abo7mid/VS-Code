from flask import Flask, flash , render_template, request, redirect, session

from mysqlconnection import connectToMySQL


app = Flask(__name__)
app.secret_key = "!@#$"

@app.route("/",methods=['POST','GET'])
def index():
	if request.method == "POST":
		mysql = connectToMySQL('mydb')
		is_valid = True
		# print(request.form)
		if len(request.form['name']) < 3:
			is_valid = False
			flash("Name should be more than 3 characters!")
			print("Name should be more than 3 characters!")

		if not (request.form['location']):
			is_valid = False
			flash("Location should not be empty!")
			print("Location should not be empty!")

		if not request.form['langs']:
			is_valid = False
			flash("language should not be empty!")
			print("language should not be empty!")

		if len(request.form['comment']) > 120:
			is_valid = False
			flash("comment should be less than 120 characters!")
			print("comment should be less than 120 characters!")

		if not is_valid:
			return redirect('/')

		else:
			if not '_flashes' in session.keys():
				query = "INSERT INTO dojo (name,location,fav_lang,comment) VALUES(%(name)s,%(location)s,%(langs)s,%(comment)s)"
				data = {

				"name" : request.form['name'],
				"location" : request.form['location'],
				"langs" : request.form['langs'],
				"comment" : request.form['comment'],
				}
				result = mysql.query_db(query,data)
				session['id'] = result
				return redirect('result')
				# print('result',result)
	return render_template('index.html')



@app.route('/result',methods=['get'])
def result():
	mysql = connectToMySQL('mydb')
	id = session['id']
	query = "SELECT * FROM dojo WHERE id = %(id)s"

	data = {
		"id":id,
	}
	result = mysql.query_db(query,data)
	# print(result)
	return render_template('result.html',result=result)


if __name__ == "__main__":
    app.run(debug=True)