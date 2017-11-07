# project-team-9

The CodeCatz project is created with the django web framework

# To start

You must create your own super user, and populate your own database. Always remember to migrate models. Also run 'python manage.py collectstatic' at first and when any new static files are added.

# account 
when server is running navigate to http://localhost:8000/account/login/ test user is setup: user/userpassword and you can add more from the superuser for now

# Adding static files
Best way to add static files is via the /static/ folder. If you want it for a specific app, create it as e.g./static/app/css or /static/app/js. This keeps all static files in the same spot. General static files are in /static/css or /static/js.


