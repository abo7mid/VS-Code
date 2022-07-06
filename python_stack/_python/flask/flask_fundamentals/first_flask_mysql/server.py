from flask import Flask, render_template
from mysqlconnection import connectToMySQL # import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('db')	# call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    print(friends)
    for friend in friends:
        print(friend['id'])
    return render_template("index.html",all_friends=friends)
            
if __name__ == "__main__":
    app.run(debug=True)

