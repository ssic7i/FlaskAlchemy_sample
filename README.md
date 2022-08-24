# Sample flask project

Example of flask project with session and SQLAlchemy

## Install dependencies:
- create virtaulenv
- pip install -r requiremenst.txt

## Run:
- python app.py

# Links:

## SQLAlchemy:
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/
- https://stackoverflow.com/questions/9692962/flask-sqlalchemy-import-context-issue/9695045#9695045

## HTML Form
- https://www.w3schools.com/tags/att_form_method.asp

## Flask Session
- https://flask-session.readthedocs.io/en/latest/
- https://www.geeksforgeeks.org/how-to-use-flask-session-in-python-flask/

## Migrations (SQLite)
- https://flask-migrate.readthedocs.io/en/latest/
- https://blog.miguelgrinberg.com/post/how-to-add-flask-migrate-to-an-existing-project
- https://github.com/sqlalchemy/alembic/issues/1062
- https://stackoverflow.com/questions/30378233/sqlite-lack-of-alter-support-alembic-migration-failing-because-of-this-solutio
- https://blog.miguelgrinberg.com/post/fixing-alter-table-errors-with-flask-migrate-and-sqlite

```
flask db init  
flask db migrate -m "migration comment"
flask db upgrade 
```