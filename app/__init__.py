from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Login module
from flask.ext.login import LoginManager

# Mail module
from flask.ext.mail import Mail



# App and database
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Login Manager
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
#lm.session_protection = 'strong' # Session protection not yet implemented nor needed

# Mail Manager
mail = Mail(app)

from app import views, models