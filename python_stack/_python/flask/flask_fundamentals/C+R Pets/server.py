from flask import Flask, redirect, render_template, request

from mysqlconnection import connectToMySQL


app = Flask(__name__)


@app.route('/',methods=['get','POST'])
def index():
    mysql = connectToMySQL("mydb")
    pets = mysql.query_db("SELECT * FROM pets")
    # for pet in pets:
    #     print(pets)
    if request.method == 'POST':
        print('post')
        mysql = connectToMySQL("mydb")
        # query = ("INSERT INTO pets (name, type) VALUES(%(name)s,%(type)s)")
        # query = "INSERT INTO pets (name, type) VALUES(%(name)s,%(type)s)"
        query = f"INSERT INTO pets (name, type) VALUES('{request.form['name']}','{request.form['type']}')" #cat'); SELECT * FROM pets WHERE id =1; #
        data = {
            "name":request.form['name'],
            "type":request.form['type']
        }
        # insert = mysql.query_db(query,data)
        pets = mysql.query_db(query)
        print(pets)
        return redirect('/')


    return render_template('index.html',pets=pets)




app.run(debug=True)