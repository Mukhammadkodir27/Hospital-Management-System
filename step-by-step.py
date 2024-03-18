# If you encounter an error with your virtual environment, run Powershell as an administrator and use below command
# Set-ExecutionPolicy RemoteSigned

# to create our virtual environment
> python -m venv my-venv 

#notice (my-venv) has to appear in your terminal, it means virtual environment is activated
(my-venv) > pip install django 

>django-admin startproject Hospital
#success

>django-admin startapp app

add "app",   in installed apps from settings.py

>python manage.py migrate
>python manage.py runserver

# success
