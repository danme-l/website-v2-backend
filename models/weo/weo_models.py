from database import db, BaseModel
    
class CountriesTable(BaseModel):
    __tablename__ = 'countries'
    __table_args__ = {'schema': 'weo', 'keep_existing': True}
    
    country_id = db.Column(db.String(6), primary_key=True)
    country = db.Column(db.String(32))

class SubjectsTable(BaseModel):
    __tablename__ = 'subjects'
    __table_args__ = {'schema': 'weo', 'keep_existing': True}

    subject_id = db.Column(db.String(12), primary_key=True)
    descriptor = db.Column(db.String(82))
    notes = db.Column(db.String(1313))
    units = db.Column(db.String(50))
    scale = db.Column(db.String(8))

class SeriesTable(BaseModel):
    __tablename__ = 'series'
    __table_args__ = {'schema': 'weo', 'keep_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.String(12))
    country_id = db.Column(db.String(6))
    estimates_start = db.Column(db.Integer)
    notes = db.Column(db.String(3264))
    year = db.Column(db.Integer)
    value = db.Column(db.Numeric(10, 4)) # TODO figure out why this gets loaded as a string on API calls