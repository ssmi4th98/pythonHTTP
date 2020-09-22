# Like a get request but it returns no info; used to see if the request will work

import requests
from pprint import pprint
import json

r_head = requests.head(("https://www.youtube.com/search"))

print(r_head.status_code)
pprint(r_head.text)

pprint(r_head.headers)  ##extract the header.

pprint(r_head.headers['Content-Length'])  ##extract particular info from the header.
pprint(r_head.headers['Content-Type'])