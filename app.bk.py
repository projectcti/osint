from flask import ( 
	Flask, render_template,
	request, jsonify
)
from emails import havei_been_pwned
import re
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index')
@app.route('/welcome')
def index():
	return render_template('index.html')

@app.route('/search/havei_been_pwned')
def search_havei_been_pwned():
	keyword = request.args.get('keyword', None)
	re_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

	if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', keyword):

	# if re.search(re_email, keyword):
		print(keyword)
		data = havei_been_pwned(keyword)
	# 	print(data)
		return jsonify(data)

	return jsonify({})

@app.route('/search', methods=['GET', 'POST'])
def search():
	re_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
	keyword = request.args.get('keyword', None)
	data = dict()

	if keyword:
		# code
		if re.search(re_email,keyword):
			pass
			# data['have_pwned'] =  havei_been_pwned(keyword)
	return render_template('search.html')