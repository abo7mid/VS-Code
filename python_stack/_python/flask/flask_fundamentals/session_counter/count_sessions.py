from crypt import methods
from flask import Flask, render_template,request,redirect,session

app = Flask(__name__)


times = 0
@app.route("/")
def index():

    global times 
    times = times + 1
    return render_template("index.html",Ttimes=times)

if __name__ == "__main__":
    app.run(debug=True)