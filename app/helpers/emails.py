import requests
import json
import os

headers = {
	'hibp-api-key': '719c61e4f75a4516b507fdfa4028f4fe'
}

hunter_key = 'ca33fe0a60af93832be64e576d316b5a34140b2c'

def havei_been_pwned(email=None):
	session = requests.Session()
	jar = requests.cookies.RequestsCookieJar()
	req = requests.get(os.environ.get("URL_HVP_EMAIL").format(email.strip(' ')), headers=headers, cookies=jar)

	if req.status_code == 200:
		return {
			'hibp_mail': req.json()
		}

	return None

def hunter(domain=None):
	session = requests.Session()
	jar = requests.cookies.RequestsCookieJar()
	req = requests.get(os.environ.get("HUNDER").format(domain.strip(' '), hunter_key), cookies=jar)
	data = req.json()
	
	if req.status_code == 200 and len(data.get('data').get('emails')) > 0:
		return {
			'domain_email': data.get('data').get('emails')
		}

	return None