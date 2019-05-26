from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cd4e828b9aecaad2b6cbaf029155ebf5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

"""
    SQLAlchemy uses models as in Django to create tables (ORM)
    When DB changes (sqlite to postgres) the python script used won't
    require any change. It'll port successfully
"""

db = SQLAlchemy(app)

from blog import routes