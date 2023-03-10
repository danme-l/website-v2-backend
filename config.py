from dotenv import dotenv_values
import os

class DevConfig:
    """database config object"""

    env = dotenv_values(".env")

    SQLALCHEMY_DATABASE_URI = f"postgresql://{env['PGUSER']}:{env['PGPWD']}@{env['PGHOST']}/{env['PGDB']}"

    # disable modification tracking for better performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig:
    """Production Config object"""

    DATABASE_URL = os.environ.get('DATABASE_URL')