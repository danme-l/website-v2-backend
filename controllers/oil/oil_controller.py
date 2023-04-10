from flask import Blueprint, jsonify
from database import db
from models.oil.oil_models import OilProductionTable
from flask_cors import cross_origin

oil_production_bp = Blueprint('oil_production', __name__)

@oil_production_bp.route('/oil_production', methods=['GET'])
@cross_origin()
def oil_production():
    oil_production = db.session.query(OilProductionTable).all()
    return jsonify([rec.serialize() for rec in oil_production])