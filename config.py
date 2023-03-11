import os

class Config:
    """Production Config object"""

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')