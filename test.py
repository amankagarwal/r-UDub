import requests
from pprint import pprint
import json

r = requests.get(r'https://www.reddit.com/user/HammerJayce/about/.json', headers = {'User-agent': 'your bot 0.1'})
python_dict = json.loads(r.text)

pprint(python_dict)
