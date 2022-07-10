path="$HOME/Assignments/python_stack/_python/flask/flask_fundamentals"
cd $path


if [ ! -d $1 ]; then
mkdir $1
cd $1
touch server.py
mkdir templates

touch templates/base.html
touch templates/index.html


base='<!DOCTYPE html>\n
<html lang="en">\n
<head>\n
    <meta charset="UTF-8">\n
    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n
    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">\n
    {%block head%}\n\n{%endblock%}\n
</head>\n
<body>\n
    {%block navbar%}\n\n{%endblock%}\n
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>\n
    <div class="container">\n
        {%block content%}\n\n{%endblock%}\n
    </div>\n
</body>\n
</html>'

index="{% extends 'base.html'%}\n
{%block head%}\n\n{%endblock%}\n
{%block navbar%}\n\n{%endblock%}\n
{%block content%}\n
<h1>test</h1>\n
{%endblock%}\n"


echo -e $index > templates/index.html
echo -e $base > templates/base.html


serverCode="from flask import Flask, render_template\n\n\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n\treturn render_template('index.html')\napp.run(debug=True)"

echo -e $serverCode > server.py


## copy mysqlconnection class to current project

#cp $path/first_flask_mysql/mysqlconnection.py .

cp $HOME/Assignments/python_stack/_python/flask/flask_fundamentals/first_flask_mysql/mysqlconnection.py .
else
	echo "project with same name exists! "
fi
