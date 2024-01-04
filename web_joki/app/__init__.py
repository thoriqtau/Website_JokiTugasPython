from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import timedelta

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = 'apaaja'
app.permanent_session_lifetime = timedelta(minutes=30)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
from app.model import user