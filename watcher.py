import requests
import hashlib
import json ## för att spara
import os ## för att kolla om filen finns

try:
    response = requests.get('https://ifkgoteborg.se/aktuell-biljettinformation/', timeout=10)
    html_content = response.text
    content_hash = hashlib.md5(html_content.encode()).hexdigest()
    ## kolla om filen finns
    if os.path.exists('state.json'):
        with open('state.json', 'r') as file:
            data = json.load(file)
            if data['hash'] == content_hash:
                print('nothig has happened')
            else:
                with open('state.json', 'w') as file_w:
                    json.dump({'hash': content_hash}, file_w)
                print('something has happened')
    else:
        ## spara till fil
        with open('state.json', 'w') as file:
            json.dump({'hash': content_hash}, file)

except requests.RequestException as e:
    print(f'Error fetching page: {e}')
    exit(1)