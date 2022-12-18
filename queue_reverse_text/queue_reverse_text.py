import sys
import requests


url = 'http://127.0.0.1:8000/queue_reverse_text/'

source_text = str(sys.argv[-1])
headers = {'Content-type': 'text/plain'}
r = requests.post(url=url, data=source_text, headers=headers)
print(r)
