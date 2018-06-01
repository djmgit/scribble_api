import datetime
from flask import Blueprint, jsonify, request
from flask import current_app as app
import json
import requests
from helpers.check_login import is_loggedin
from helpers.query_all_notes import query_all

router = Blueprint('all_notes', __name__)

@router.route('/all_notes', methods=['GET'])
def add_note():
	response = ""

	auth_token = request.headers.get('Authorization')
	if not auth_token or auth_token == "":
		response = {"status": "auth token not specified"}
		auth_token = "03f2082d255ecb0ede1cc760d65601ec0cd99dc90fa3193a"

	hasura_id = is_loggedin(auth_token)
	if not hasura_id:
		response = {"status": "User is not logged in. Please login first"}
		return jsonify(response)

	response = query_all(hasura_id)
	return jsonify(response)
