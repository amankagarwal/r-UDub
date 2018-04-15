import requests
from pprint import pprint
import json

r = requests.get(r'https://www.reddit.com/r/udub/top.json', headers = {'User-agent': 'your bot 0.1'})
# I can get number of upvotes
# I can get the link of the post with the comments "permalink"
# I can get the title of the post which is a good indicator of what
# type of post it is.
python_dict = json.loads(r.text)
pprint(python_dict)
