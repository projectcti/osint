from flask import ( 
	Flask, render_template,
	request, jsonify
)
import re
import json
def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    # import blueprints
    from app.views.home import home_app
    from app.views.api import api_app

    # register blueprints
    app.register_blueprint(home_app)
    app.register_blueprint(api_app, url_prefix='/api')

    return app
