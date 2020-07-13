import requests
import json
import os


def search_shodan_ip(ip=None):
    session = requests.Session()
    jar = requests.cookies.RequestsCookieJar()
    req = requests.get(os.environ.get("URL_HVP_EMAIL").format(email.strip(' ')), headers=headers, cookies=jar)
    
    if req.status_code == 200:
        return {
            'hibp_mail': req.json()
        }
    
    return None