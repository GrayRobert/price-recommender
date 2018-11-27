Note this is so far just a django shell of a project to get a basic API up before pluggin in the machine learning model

# Load the Python Virtual Environment
source venv/bin/activate

# Run the API
cd to src directory
python manage.py runserver

# Database ORM
Django has some object relational model features so we can persist our models into a database with schemas

## Generate the schemas
python manage.py makemigrations recommender

## Persist the schemas
python manage.py migrate