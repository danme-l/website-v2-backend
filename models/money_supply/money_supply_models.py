from database import db, BaseModel

class MoneySupplyTable(BaseModel):
    __tablename__ = 'money_supply'
    __table_args__ = {'schema': 'money', 'keep_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    value = db.Column(db.Numeric(10, 4))
    type = db.Column(db.String(2))
    country = db.Column(db.String(3))