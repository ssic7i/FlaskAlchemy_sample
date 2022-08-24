import os.path
import uuid

from flask import Flask, render_template, request, session
from flask_session import Session
from flask_migrate import Migrate
from models import db
import views


def get_app_secret():
    if os.path.exists('app_secret'):
        secret_file = open('app_secret')
        secret_data = secret_file.read()
        secret_file.close()
    else:
        secret_file = open('app_secret', 'w')
        secret_data = str(uuid.uuid4())
        secret_file.write(secret_data)
        secret_file.close()
    return secret_data


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
db.init_app(app)
migrate = Migrate(app, db, render_as_batch=True)
app.secret_key = get_app_secret()
Session(app)

@app.route('/')
def hello_handler():
    return render_template('hello.html')

@app.route('/database')
def database_handler():
    view_data = views.get_users()
    return render_template('db_page.html', users=view_data)


@app.route("/login", methods=["POST", "GET"])
def login_handler():
    if request.method == "POST":
        session["name"] = request.form.get("name")
    return render_template("login.html", session_data=str(session), request_method=request.method)


if __name__ == '__main__':
    app.run()
