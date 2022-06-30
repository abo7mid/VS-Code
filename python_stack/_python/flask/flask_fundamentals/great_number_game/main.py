from crypt import methods
from random import randint
from django.shortcuts import redirect
from flask import Flask, render_template, session, request, url_for
# from webargs import flaskparser,fields

app = Flask(__name__)
app.secret_key = "123"


# in the root route, save a random number between 1 and 100
# and display a form for the user to guess the number

# Create a route that determines whether the number submitted is
# too high, too low, or correct. Show this status on the HTML page.
# Form_ARGS = {
#     'num' : fields.Str(requesired=True),
# }



@app.route("/", methods=['GET','POST'])
def gng():
    # get a value from a session that was created in other function
    session['genNum'] = int(randint(1, 5))    
    if request.method == 'POST':
        print('POST')
        if request.form.get('num'):
            # print("empty input")
            # return redirect('/')
            genNum = session['genNum']
            userInput = int(request.form['num'])  # take userinput
            print(f"userinput {userInput} generated num {genNum}") # debugging
    
            if userInput > genNum:
                value = "high"
            elif userInput < genNum:
                value = "low"
            elif userInput == genNum:
                value = "hit"
            print(value)
            context = {
            "genNum": session['genNum'],
            "userInput": int(request.form['num']),
            "value":value
            }

    if request.method == "GET":
        print('GET')
        context = {
                "genNum": session['genNum'],
        }
    return render_template('index.html',context=context)
    # return redirect(url_for('/',context=context)) wrong to use this ?


app.run(debug=True)
