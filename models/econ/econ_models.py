from database import db, BaseModel

class HouseholdDebtTable(BaseModel):
    __tablename__ = 'household_debt'
    __table_args__ = {'schema': 'econ', 'keep_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    value = db.Column(db.Numeric(10, 4))
    country = db.Column(db.String(18))