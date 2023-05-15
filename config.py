import os
from dotenv import load_dotenv


load_dotenv()

basedir= os.path.abspath(os.path.dirname(__file__))

class Config():
    FLASK_APP = os.environ.get("FLASK_APP")
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI =os.environ.get("SQLALCHEMY_DATABASE_URI")