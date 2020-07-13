import os
import re
from flask import ( 
    Blueprint,
    render_template,
    request, current_app,
    jsonify
)
from app.helpers.emails import havei_been_pwned, hunter

api_app = Blueprint('api_app', __name__)

@api_app.route('/search', methods=['GET', 'POST'])
def api_search():
    keyword = request.args.get('keyword', None)

    if re.search(os.environ.get("RE_EMAIL"),keyword):
        data = havei_been_pwned(keyword)
        if data:
            return jsonify(data)
        else:
            return jsonify({})

    if re.search(os.environ.get("RE_DOMAIN"),keyword):
        data = hunter(keyword)
        if data:
            return jsonify(data)
        else:
            return jsonify({})

    return {}