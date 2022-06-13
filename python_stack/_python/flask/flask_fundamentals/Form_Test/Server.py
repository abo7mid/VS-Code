from glob import glob
from flask import Flask, render_template, request, redirect ,session

app = Flask(__name__)
app.secret_key = "123"

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")



@app.route('/users',methods=['POST'])
def create_user():
    print(request.form)
    session['name'] = request.form['name']
    session['email'] = request.form['email']

    # we could use global var instead of sessions
    # I'm not sure if this is a good prictise for now
    # global name 
    # name = request.form['name']
    # global email 
    # email = request.form['email']
    
    return redirect("/show")
    # return render_template('show.html',template_name=form_name,template_email=form_email)


@app.route("/show") #when someone request this route response with show.html 
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template('show.html')
    # return render_template("show.html",template_name=name,template_email=email)


if __name__ == "__main__":
    app.run(debug=True)

