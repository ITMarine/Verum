import sys
import requests


URL = 'http://127.0.0.1:8000/queue_reverse_text/'

source_text = str(sys.argv[-1])
headers = {'Content-type': 'text/plain'}
params = {'source_text': source_text}
r = requests.get(url=URL, params=params, headers=headers)
print(r)
