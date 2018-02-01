# Django-Test


```
sudo apt-get install python3-venv
```
It will create virtualenv
```
python3 -m venv env ###Virtualenv 
```
Activate the virtual environment 
```
source env/bin/activate
```
Install Django with pip:
```
pip install django==1.11.7
```
Creating a project. (Election is project name.)
```
django-admin startproject election .
```

### /election directory
This folder will contain all the files of the project.

* __init__.py It allows the folder we created to be recognized as a python module.It will always be empty.

* settings.py Here are all the settings and configurations related to the project.

* urls.py Includes the project map. All addresses here

* wsgi.py Django includes the development server.

* manage.py Used to start the Django server.

This command allows us to run.
```
python manage.py runserver 
```
Create the migration and 
```
python manage.py makemigrations election
python manage.py makemigrations profile
```

Apply the migration:
```
python manage.py migrate
```

server’s actual IP: http://127.0.0.1:8000

Admin Panel: http://127.0.0.1:8000/admin
