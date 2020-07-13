from flask import Blueprint, render_template
home_app = Blueprint('home_app', __name__)

@home_app.route('/', methods=['GET'])
@home_app.route('/index')
@home_app.route('/welcome')
def index():
	return render_template('index.html')