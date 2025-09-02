import requests
import hashlib
import json
import os
import config
from bs4 import BeautifulSoup


def save_hash(hash_value):
    with open('state.json', 'w') as file:
        json.dump({'hash': hash_value}, file)

def load_hash():
    with open('state.json', 'r') as file:
        state_data = json.load(file)
        return state_data['hash']

def check_for_changes():
    script_config = config.read_config()
    selector = script_config['css_selector']
    response = requests.get(script_config['url'], timeout=10)
    html_content = response.text
    element = BeautifulSoup(html_content, 'html.parser').select_one(selector)
    if element:
        monitored_text = element.get_text()
    else:
        return False
    
    content_hash = hashlib.md5(monitored_text.encode()).hexdigest()
    if os.path.exists('state.json'):
        hash_data = load_hash()
        if hash_data == content_hash:
            return False
        else:
            save_hash(content_hash)
            return True
    else:
        save_hash(content_hash)
        return False