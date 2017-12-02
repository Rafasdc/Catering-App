# project-team-9

The CodeCatz project is created with the django web framework

# To start

You must create your own super user, and populate your own database. Always remember to migrate models. Also run 'python manage.py collectstatic' at first and when any new static files are added.

# account 
when server is running navigate to http://localhost:8000/account/login/ test user is setup: user/userpassword and you can add more from the superuser for now

# Adding static files
Best way to add static files is via the /static/ folder. If you want it for a specific app, create it as e.g./static/app/css or /static/app/js. This keeps all static files in the same spot. General static files are in /static/css or /static/js.

#To Run
You need to have python 3+, and install with pip:
django
django_extensions
django-celery
django-autocomplete-light
requests

After installing navigate to CodeCatz main folder and run
python manage.py runserver

This should start the server at localhost:8000

Some users that can be used are:
User/Password (both are case sensitive)
Manager: manager/manager123
Employee: Waiter1/employee123
Regular User: JoeUser/user1234

To access the admin go to localhost:8000/admin/
You need a super user to access the admin, you can create one with
python manage.py createsuperuser

Note: that running the server inside a virtualenv, may produce SSL error when trying to connect to the external API to get temp employees. 
