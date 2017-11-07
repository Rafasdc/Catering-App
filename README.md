# project-team-9

The CodeCatz project is created with the django web framework

# To start

You must create your own super user, and populate your own database. Always remember to migrate models. Also run 'python manage.py collectstatic' at first and when any new static files are added.

# Auto-population
For auto-population of databases, run python manage.py populate_db. To add items to populate_db, load catering/management/commands/populate_db.py and edit it and add what you think is important. There is an example showcasing the syntax, add a function for the model you're populating.

# account 
when server is running navigate to http://localhost:8000/account/login/ test user is setup: user/userpassword and you can add more from the superuser for now


