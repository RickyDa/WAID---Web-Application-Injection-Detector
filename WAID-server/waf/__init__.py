##################################################
import datetime

from flask_mail import Mail

from logger.log import log
from config.config_handler import Config
##################################################
from pathlib import Path
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
##################################################
import secrets

##################################################
log = log
config = Config()
app = Flask(__name__)
app.config['SECRET_KEY'] = config.get_value('SECRET_KEY', secrets.token_hex(16))
# Hard Coded
app.config['SQLALCHEMY_DATABASE_URI'] = config.get_value('SQLALCHEMY_DATABASE_URI', 'sqlite:///database/server.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)
# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = config.get_value('SECRET_KEY', secrets.token_hex(16))
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
jwt = JWTManager(app)
jwt._set_error_handler_callbacks(app)
app.config.update(dict(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=config.get_value("mail", "waidwaf@gmail.com"),
    MAIL_PASSWORD=config.get_value("mail_pass", "rickyronen"),
))
mail = Mail(app)
from waf.layout.rule import rule_control
from waf.layout.user import user_control
from waf.layout.config import config_control
from waf.layout.proxy import proxy
from waf.scheduler import sched

base_path = Path(__file__).parent
file_path = (base_path / "./database/server.db").resolve()
sched.start()
if not file_path.is_file():
    from waf.database.models import User
    from waf.logic import rule_service, user_service

    db.drop_all()
    db.create_all()
    user_service.create(User(username='admin', password='admin', mail='admin@admin.com', role=0))
    log.debug("DB Created")
