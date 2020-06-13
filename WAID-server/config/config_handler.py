import configparser
from pathlib import Path
import secrets
from waf import log

FILE_PATH = (Path(__file__).parent / 'config.ini').resolve()
CONFIG_PARSER = configparser.ConfigParser()
private_conf_list = ["secret_key", "sqlalchemy_database_uri"]


class Config:

    def __init__(self):
        if not FILE_PATH.is_file():
            self.create_config()
        else:
            CONFIG_PARSER.read(str(FILE_PATH))

    @staticmethod
    def create_config():
        CONFIG_PARSER['GENERAL'] = {
            'site_address': 'https://redtiger.labs.overthewire.org/',
            'SECRET_KEY': secrets.token_hex(16),
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///database/server.db',
            'is_client': True,
            'server_ip': '',
            'is_active': True,
            'is_analyzer': True,
            'is_classifier': True,
            'mail': "waidwaf@gmail.com",
            'mail_password': "rickyronen"
        }
        with open(str(FILE_PATH), 'w') as configfile:
            CONFIG_PARSER.write(configfile)

    @staticmethod
    def get_value(key, default):
        try:
            return CONFIG_PARSER.get('GENERAL', key)
        except (configparser.NoOptionError, KeyError):
            log.error(f"Key - '{key}' dont exist in the config file, using default value - {default}.")
            return default

    @staticmethod
    def set_value(key, value):
        try:
            CONFIG_PARSER.set('GENERAL', key, value)
            with open(str(FILE_PATH), 'w') as configfile:
                CONFIG_PARSER.write(configfile)
                return True
        except (configparser.NoSectionError, TypeError):
            # log.exception(f"Key - '{key}' dont exist in the config file, using default value - {default}.")
            return None

    @staticmethod
    def get_all_web():
        to_client_dict = {}
        props = dict(CONFIG_PARSER.items(section='GENERAL'))
        for k, v in props.items():
            if k not in private_conf_list:
                to_client_dict[k] = v
        return to_client_dict
