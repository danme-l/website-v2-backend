from dotenv import dotenv_values

class Config:
    """database config object"""

    env = dotenv_values(".env")

    SQLALCHEMY_DATABASE_URI = f"postgresql://{env['PGUSER']}:{env['PGPWD']}@{env['PGHOST']}/{env['PGDB']}"

    # disable modification tracking for better performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False