import requests
import hashlib
import json
import os
import config


def save_hash(hash_value):
    with open('state.json', 'w') as file:
        json.dump({'hash': hash_value}, file)

def load_hash():
    with open('state.json', 'r') as file:
        state_data = json.load(file)
        return state_data['hash']

def check_for_changes():
    script_config = config.read_config()
    response = requests.get(script_config['url'], timeout=10)
    html_content = response.text
    content_hash = hashlib.md5(html_content.encode()).hexdigest()
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