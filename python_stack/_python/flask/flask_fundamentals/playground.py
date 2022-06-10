from flask import Flask, render_template, get_template_attribute

app = Flask(__name__)

@app.route("/play")
def play():
    return render_template("play1.html")




@app.route("/play/<int:times>")
def playTimes(times):
    return render_template("play2.html",times=int(times))
    # what if we want to render the same page




@app.route("/play/<int:times>/<string:color>")
def playTimesAndColor(times,color):
    return render_template("play3.html",times=int(times),color=color)





@app.errorhandler(404)
def NotFound(e):
    return "Page Not Found"




if __name__ == "__main__":

    app.run(debug=True)