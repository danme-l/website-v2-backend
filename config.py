import os

class Config:
    """Production Config object"""

    DATABASE_URL = os.environ.get('DATABASE_URL')