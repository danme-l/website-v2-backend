from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

class BaseModel(db.Model):
    __abstract__ = True

    def serialize(self):
        """
        converts database records to JSON format 
        by adding each attribute name and value to the dict
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}