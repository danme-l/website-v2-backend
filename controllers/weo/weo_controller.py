from flask import Blueprint, jsonify, request
from database import db
from models.weo.weo_models import CountriesTable, SubjectsTable, SeriesTable

weo_bp = Blueprint('weo_bp', __name__)

@weo_bp.route('/weo/countries')
def get_countries():
    countries = db.session.query(CountriesTable).all()
    return jsonify([rec.serialize() for rec in countries]), 200

@weo_bp.route('/weo/subjects', methods=['GET'])
def get_subjects():
    subjects = SubjectsTable.query.all()
    return jsonify([rec.serialize() for rec in subjects]), 200

@weo_bp.route('/weo/series', methods=['GET'])
def get_series():
    country_id = request.args.get('countryId')
    subject_id = request.args.get('subjectId')

    if not country_id or not subject_id:
        return jsonify({'error': 'Missing countryId or subjectId param'}), 400

    series = SeriesTable.query.filter_by(country_id=country_id, subject_id=subject_id).all()

    for s in series:
        s.value = float(s.value)
        
    return jsonify([rec.serialize() for rec in series]), 200