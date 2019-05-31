from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cd4e828b9aecaad2b6cbaf029155ebf5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

"""
    Bcrypt used to hash passwords
"""
bcrypt = Bcrypt(app)
"""
    LoginManager used to handle sessions
"""
login_manager = LoginManager(app)
login_manager.login_view = 'login'

"""
    SQLAlchemy uses models as in Django to create tables (ORM)
    When DB changes (sqlite to postgres) the python script used won't
    require any change. It'll port successfully
"""

db = SQLAlchemy(app)

from blog import routes