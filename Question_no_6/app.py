from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json


app= Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from route import *

if __name__=='__main__':
    app.run()
