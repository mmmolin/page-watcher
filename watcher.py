import requests
import hashlib
import json ## för att spara
import os ## för att kolla om filen finns


def save_hash(hash_value):
    with open('state.json', 'w') as file:
        json.dump({'hash': hash_value}, file)

def load_hash():
    with open('state.json', 'r') as file:
        state_data = json.load(file)
        return state_data['hash']

try:
    response = requests.get('https://ifkgoteborg.se/aktuell-biljettinformation/', timeout=10)
    html_content = response.text
    content_hash = hashlib.md5(html_content.encode()).hexdigest()

    if os.path.exists('state.json'):
        hash_data = load_hash()
        if hash_data == content_hash:
            print('nothing has happened')
        else:
            save_hash(content_hash)
            print('something has happened')
    else:
        save_hash(content_hash)

except requests.RequestException as e:
    print(f'Error fetching page: {e}')
    exit(1)