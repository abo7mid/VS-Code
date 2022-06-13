
from flask import Flask , render_template, request, redirect


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')



@app.route('/result',methods=['POST'])
def result():
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    langs = request.form['langs']
    comment = request.form['comment']
    return render_template('result.html',html_name=name,html_location=location,html_fav_lang=langs,html_comment=comment)


if __name__ == "__main__":
    app.run(debug=True)