path='$HOME/Assignments/python_stack/_python/flask/flask_fundamentals'
cd $path
mkdir $1
cd $1
touch server.py
mkdir templates

touch templates/base.html
touch templates/index.html




base='<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    {%block head%}{%endblock%}
</head>
<body>
    {%block navbar%}{%endblock%}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
    <div class="container">
        {%block content%}{%endblock%}
    </div>
</body>
</html>'

index="{% extends 'base.html'%}
{%block head%}{%endblock%}
{%block navbar%}{%endblock%}
{%block content%}
<h1>test</h1>
{%endblock%}"


echo index > templates/index.html
echo base > templates/base.html


serverCode="from flask import Flask, render_template\n\n\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n\treturn render_template('index.html')\napp.run(debug=True)"

echo -e $serverCode > server.py


## copy mysqlconnection class to current project

cp $path/first_flask_mysql/mysqlconnection.py .