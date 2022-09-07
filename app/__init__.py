#import flask and/or important modules or extensions

from flask_wtf.csrf import CSRFProtect
from flask import Flask , session
from flask_session import Session

from dotenv import load_dotenv
import config
import os
from flask import Blueprint , render_template
from werkzeug.utils import secure_filename
# from . import *
# from .models import *

# create app object

app=Flask(__name__)
app.secret_key = 'askl#&*jkllsa23'
csrf = CSRFProtect(app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = "D:/programming/ITI/Flask/alproject/app/static/uploads"
ALLOWED_EXTNSIONS = set(['png','jpg','jpeg','gif','jpeg'])


# environment configuartions

APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dotenv_path = os.path.join(APP_ROOT, ".env")

load_dotenv(dotenv_path)
app.config.from_object('config.settings.' + os.environ.get('ENV'))


# database


from app.models import db ,myusers
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/aiproject'


db = SQLAlchemy(app)


db.create_all()
db.session.commit()




# error handling

@app.errorhandler(404)
def notfound(error):
    title='Not Found'
    return render_template('error/notfound.html',title=title) , 404


# add home Blueprint
from app.views.home import home as home_blueprint

# add auth Blueprint
from app.views.auth import auth as auth_blueprint


# register home blueprint in my app
app.register_blueprint(home_blueprint)

# register auth blueprint in my app
app.register_blueprint(auth_blueprint)