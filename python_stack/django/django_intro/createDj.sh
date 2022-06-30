django-admin startproject $1
cd $1
python manage.py startapp $2

sed -i '14 i from django.contrib import messages' $1/settings.py
sed -i "39 i'$2', " $1/settings.py ##we need a tab befor 'app_one'
sed -i "42 i MESSAGE_TAGS = {\n\nmessages.ERROR:'danger'\n} " $1/settings.py
#done with settings.py



sed -i "18 i from django.urls import include" $1/urls.py
sed -i "21 i path('',include('$2.urls'))," $1/urls.py
#done with project urls.py

cd $2

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
#done with the templates

sed -i "3 i def index(request):\n\treturn render(request,'index.html')" views.py
#done with app views.py


echo "#" > urls.py # sed cannot write to empty files, so # do the trick
sed -i "1 i from django.urls import path" urls.py
sed -i "2 i from  . import views\n\n" urls.py
sed -i "3 i urlpatterns = [\n\tpath('', views.index, name='index'),\n]" urls.py
#done with app urls.py