import os
from dotenv import dotenv_values

class Config:
    """Production Config object"""

    # old config string
    env = dotenv_values(".env")

    SQLALCHEMY_DATABASE_URI = f"postgresql://{env['PGUSER']}:{env['PGPWD']}@{env['PGHOST']}/{env['PGDB']}"
    # postgresql://{env['PGUSER']}:{env['PGPWD']}@{env['PGHOST']}/{env['PGDB']}

    # SQLAlchemy doesn't accept 'postgres://' anymore, but this is render's default
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://")