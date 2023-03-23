from flask import Flask, request, jsonify
from config import Config
from flask_cors import CORS, cross_origin
from database import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.config['CORS_HEADERS'] = 'Content-Type'

    db.init_app(app)

    # import controllers
    from controllers.weo.weo_controller import weo_bp
    from controllers.econ.econ_controller import econ_bp

    # register controllers
    app.register_blueprint(weo_bp)
    app.register_blueprint(econ_bp, url_prefix='/econ')

    # test route
    @app.route('/')
    def hello_world():
        return "Hello, World!"

    # error handler
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not Found"}), 404

    return app

app = create_app()
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response



if __name__ == '__main__':
    app.run()