from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',phrase="hello",times=10)


@app.route('/dojo')

def dojo():
    return "Dojo!"


@app.route('/say/<name>')

def say(name):
    return f"Hi  {name}!" 



@app.route('/repeat/<int:times>/<word>')
def checkInt(times,word):
        print(word*int(times))
        return f"{word} " * int(times)


@app.route('/repeat/<string:times>/<word>')
def checkStr(times,word):
    return "must be an integer"


@app.errorhandler(404)
def page_not_Found(e):
    print("404")
    return "Sorry! No response. Try again."




if __name__ == "__main__":
    app.run(debug=True)
