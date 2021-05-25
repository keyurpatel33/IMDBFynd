import os

from app import app
from flask_sqlalchemy import SQLAlchemy

URI = "mysql://{}:{}@{}/{}".format(
    
    
    os.environ.get('MYSQL_ADDON_USER'),
    os.environ.get('MYSQL_ADDON_PASSWORD'),
    os.environ.get('MYSQL_ADDON_HOST'),
    os.environ.get('MYSQL_ADDON_DB')
)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = URI
db = SQLAlchemy(app)
