import requests
from pprint import pprint
import json

r_get = requests.get("http://swapi.dev/api/vehicles/1")

print(pprint(r_get.status_code))

print((pprint(r_get.headers)))

data = json.loads(r_get.text)  #returns body on GET in json format
print(pprint(data))




