from random import randint
from flask import Flask, redirect,session, render_template, request, template_rendered

app = Flask(__name__)
app.secret_key = "123"


@app.route('/',methods=['GET'])
def main():
    session['allgold'] = 0

    if request.method == 'GET':
        print('GET')
        context = {

        "allgold": session['allgold']
    }
        return render_template('index.html',context=context)






from time import strftime,gmtime
@app.route('/process_money',methods=['POST'])
def process():    
    if request.form.get('which_form') == 'farm' or request.form.get('which_form') == 'cave' or request.form.get('which_form') == 'house':
        
        current_gold = randint(1,20)
        session['allgold'] = session['allgold'] + current_gold
        date = strftime("%m-%d-%Y %H:%M %p", gmtime())
        text = f"You entered a {request.form.get('which_form')} and earned {current_gold} gold. ({date})"


        context = {

        "allgold": session['allgold'],
        "text":text,
        "color":"green"
        }
        return render_template('index.html',context=context)




    if request.form.get('which_form') == 'quest':    
        current_gold = randint(0,50)
        date = strftime("%m-%d-%Y %H:%M %p", gmtime())
        if current_gold % 2 == 0: 
            session['allgold'] = session['allgold'] + current_gold
            color = "green"
            text = f"You entered a {request.form.get('which_form')} and earned {current_gold} gold. ({date})"
        else:
            session['allgold'] = session['allgold'] - current_gold
            color = "red"
            text = f"You entered a {request.form.get('which_form')} and lost {current_gold} gold. ({date})"
   

        context = {

        "allgold": session['allgold'],
        "text":text,
        "color":color
        }   
        return render_template('index.html',context=context)


app.run(debug=True)