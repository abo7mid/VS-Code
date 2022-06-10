from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def checkerboard():
    return render_template("checkerboard.html")

@app.route("/<int:boxY>")
def checkerboard1(boxY):
    return render_template("checkerboard1.html",boxY=int(boxY))



@app.route("/<int:boxY>/<int:boxX>")
def checkerboard2(boxY,boxX):
    return render_template("checkerboard2.html",boxY=int(boxY),boxX=int(boxX))



@app.errorhandler(404)
def PageNotFound(e):
    return "page not found"
if __name__ == "__main__":
    app.run(debug=True)