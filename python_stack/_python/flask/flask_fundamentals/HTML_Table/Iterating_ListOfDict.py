from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")

def ListOfDict():
    users = [
        {'firstname':'Michael','lastname':'Choi'},   #users[0][firstname] Muhammed
        {'firstname':'John','lastname':'Supsupin'},
        {'firstname':'Mark','lastname':'Guillen'},
        {'firstname':'KB','lastname':'Tonel'},
        {'firstname':'Ahmed','lastname':'Nadawi'}
    ]
    return render_template("table.html",users=users)


@app.errorhandler(404)
def pageNofFound(e):
    return "<title>الصفحة غير موجودة</title><h1>page not found 404</h1>"
if __name__ == "__main__":
    app.run(debug=True)