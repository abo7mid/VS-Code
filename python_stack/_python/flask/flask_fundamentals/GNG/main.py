from crypt import methods
from glob import glob
from random import randint
from flask import Flask, render_template, session, request


app = Flask(__name__)
app.secret_key = "123"

global num 
num = None

# in the root route, save a random number between 1 and 100
# and display a form for the user to guess the number
@app.route("/")
def gng():
    num = randint(1, 10)
    return render_template('index.html',Tnum=num)




# Create a route that determines whether the number submitted is 
# too high, too low, or correct. Show this status on the HTML page.
@app.route('/', methods=['POST'])
def guess():
    # form_num = int(request.form['num'])
    session['num'] = int(request.form['num'])
    print(f"generated num {num} value {session['num']}")


    # if session['num'] == num:
        # print("there are equal")
    #     return render_template('found.html')
    # else:
    #     return render_template('found.html')
    return render_template('index.html')


app.run(debug=True)