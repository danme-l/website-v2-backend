import os
from dotenv import dotenv_values

class Config:
    """Production Config object"""

    # SQLAlchemy doesn't accept 'postgres://' anymore, but this is render's default
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://")