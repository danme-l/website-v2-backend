from database import db, BaseModel
from models.custom_types.custom_types import CustomNumeric

class OilProductionTable(BaseModel):
    __tablename__ = 'oil_production_yearly'
    __table_args__ = {'schema': 'oil', 'keep_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    country = db.Column(db.String(3))
    value = db.Column(CustomNumeric(10, 4))
    in_opec = db.Column(db.Integer)