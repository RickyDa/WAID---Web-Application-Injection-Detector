##################################################
from logger.log import log
from config.config_handler import Config
##################################################
from pathlib import Path
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
##################################################
import secrets
##################################################

log = log
config = Config()
app = Flask(__name__)
app.config['SECRET_KEY'] = config.get_value('SECRET_KEY', secrets.token_hex(16))
app.config['SQLALCHEMY_DATABASE_URI'] = config.get_value('SQLALCHEMY_DATABASE_URI','sqlite:///database/server.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)
from waf.layout.rule import rule_control
from waf.layout.user import user_control
from waf.layout.config import config_control
from waf.layout.proxy import proxy

base_path = Path(__file__).parent
file_path = (base_path / "./database/server.db").resolve()

if not file_path.is_file():
    db.drop_all()
    db.create_all()
    log.debug("DB Created")
