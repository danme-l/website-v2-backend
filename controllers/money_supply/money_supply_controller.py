from flask import Blueprint, jsonify
from database import db
from models.money_supply.money_supply_models import MoneySupplyTable
from flask_cors import cross_origin

money_supply_bp = Blueprint('money_supply_bp', __name__)

@money_supply_bp.route('/money_supply', methods=['GET'])
# @cross_origin()
def money_supply():
    money_supply = db.session.query(MoneySupplyTable).all()
    return jsonify([rec.serialize() for rec in money_supply])