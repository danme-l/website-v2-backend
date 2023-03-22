from flask import Blueprint, jsonify
from database import db
from models.econ.econ_models import HouseholdDebtTable
from flask_cors import cross_origin

econ_bp = Blueprint('econ_bp', __name__)

@econ_bp.route('/household_debt', methods=['GET'])
@cross_origin()
def get_household_debt():
    hh_debt = db.session.query(HouseholdDebtTable).all()
    return jsonify([rec.serialize() for rec in hh_debt])