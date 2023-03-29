import os
from route import app
#database connection
project_dir = os.path.dirname(os.path.abspath(__file__))

database_file = "sqlite:///{}".format(os.path.join(project_dir,"storedatabase.db"))
app.config["SQLALCHEMY_DATABASE_URI"]=database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
