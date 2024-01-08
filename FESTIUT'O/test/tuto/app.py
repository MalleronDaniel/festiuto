from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
import os.path

def mkpath(p):
    return os.path.normpath(os.path.join(os.path.dirname( __file__ ),p))

app = Flask( __name__ )

login_manager = LoginManager(app)
login_manager.login_view = "login"

app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../myapp.db'))
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = "caf7e98a-a997-4d08-9665-bfea016ff37d"