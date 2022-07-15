django-admin startproject $1
cd $1
python manage.py startapp $2

sed -i '14 i from django.contrib import messages' $1/settings.py
sed -i "41 i'$2', " $1/settings.py ##we need a tab befor 'app_one'
sed -i "43 i MESSAGE_TAGS = {\n\nmessages.ERROR:'danger'\n} " $1/settings.py
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




gitignore="
# Django #\n
\r*.log\n
\r*.pot\n
\r*.pyc\n
\r__pycache__\n
\rdb.sqlite3\n
\rmedia\n
\r# Backup files #\n
\r*.bak\n
\r# If you are using PyCharm #\n
\r# User-specific stuff\n
\r.idea/**/workspace.xml\n
\r.idea/**/tasks.xml\n
\r.idea/**/usage.statistics.xml\n
\r.idea/**/dictionaries\n
\r.idea/**/shelf\n
\r# AWS User-specific\n
\r.idea/**/aws.xml\n
\r# Generated files\n
\r.idea/**/contentModel.xml\n
\r# Sensitive or high-churn files\n
\r.idea/**/dataSources/\n
\r.idea/**/dataSources.ids\n
\r.idea/**/dataSources.local.xml\n
\r.idea/**/sqlDataSources.xml\n
\r.idea/**/dynamic.xml\n
\r.idea/**/uiDesigner.xml\n
\r.idea/**/dbnavigator.xml\n
\r# Gradle\n
\r.idea/**/gradle.xml\n
\r.idea/**/libraries\n
\r# File-based project format\n
\r*.iws\n
\r# IntelliJ\n
\rout/\n
\r# JIRA plugin\n
\ratlassian-ide-plugin.xml\n
\r# Python # \n
\r*.py[cod] \n
\r*$py.class \n
\r# Distribution / packaging \n
\r.Python build/ \n
\rdevelop-eggs/ \n
\rdist/ \n
\rdownloads/ \n
\reggs/ \n
\r.eggs/ \n
\rlib/ \n
\rlib64/ \n
\rparts/ \n
\rsdist/ \n
\rvar/ \n
\rwheels/ \n
\r*.egg-info/ \n
\r.installed.cfg \n
\r*.egg \n
\r*.manifest \n
\r*.spec \n
\r# Installer logs \n
\rpip-log.txt \n
\rpip-delete-this-directory.txt \n
\r# Unit test / coverage reports \n
\rhtmlcov/ \n
\r.tox/ \n
\r.coverage \n
\r.coverage.* \n
\r.cache \n
\r.pytest_cache/ \n
\rnosetests.xml \n
\rcoverage.xml \n
\r*.cover \n
\r.hypothesis/ \n
\r# Jupyter Notebook \n
\r.ipynb_checkpoints \n
\r# pyenv \n
\r.python-version \n
\r# celery \n
\rcelerybeat-schedule.* \n
\r# SageMath parsed files \n
\r*.sage.py \n
\r# Environments \n
\r.env \n
\r.venv \n
\renv/ \n
\rvenv/ \n
\rENV/ \n
\renv.bak/ \n
\rvenv.bak/ \n
\r# mkdocs documentation \n
\r/site \n
\r# mypy \n
\r.mypy_cache/ \n
\r# Sublime Text # \n
\r*.tmlanguage.cache \n
\r*.tmPreferences.cache \n
\r*.stTheme.cache \n
\r*.sublime-workspace \n
\r*.sublime-project \n
\r# sftp configuration file \n
\rsftp-config.json \n
\r# Package control specific files Package \n
\rControl.last-run \n
\rControl.ca-list \n
\rControl.ca-bundle \n
\rControl.system-ca-bundle \n
\rGitHub.sublime-settings \n
\r# Visual Studio Code # \n
\r.vscode/* \n
\r!.vscode/settings.json \n
\r!.vscode/tasks.json \n
\r!.vscode/launch.json \n
\r!.vscode/extensions.json \n
\r.history\n
\r.vscode/extensions.json\n
\r.vscode/launch.json\n
\r.vscode/settings.json\n
\r.vscode/extensions.json\n
\r.vscode/launch.json\n
\r.vscode/settings.json\n"


echo $index > templates/index.html
echo $base > templates/base.html
#done with the templates

sed -i "3 i def index(request):\n\treturn render(request,'index.html')" views.py
#done with app views.py


echo "#" > urls.py # sed cannot write to empty files, so # do the trick
sed -i "1 i from django.urls import path" urls.py
sed -i "2 i from  . import views\n\n" urls.py
sed -i "3 i urlpatterns = [\n\tpath('', views.index, name='index'),\n]" urls.py
#done with app urls.py

#pwd
touch ../.gitignore
echo -e $gitignore > ../.gitignore
cd ../ ;python manage.py runserver
