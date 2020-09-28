import requests
import json
from pprint import pprint

r_get = requests.get('http://swapi.dev/api/vehicles/4/')

print(r_get.content)

pprint(r_get.json())

# to query whether json is available query the header for content-type

print(r_get.headers['content-type'])

r_get1 = requests.get('https://yahoo.com')

print(r_get1.headers['content-type'])

r_get2 = requests.get('https://maps.googleapis.com/maps/api/geocode/json')

print(r_get2.headers['content-type'])

r_get3 = requests.get('http://swapi.dev/api/vehicles/4/',stream=True) # here we set stream to true to handle large amounts of data.

print(r_get3.raw)
# to read the raw response - first ten characters:

print(r_get3.raw.read(10))

#  this can be done using a "with" statement to read the downloaded files:

with requests.get('http://swapi.dev/api/vehicles/4/',stream=True) as response:
    with open('raw_file.txt','wb') as b:
        for chunk in response.iter_content(1000):  #sets chunk size so not to overload the system on download
            b.write(chunk)

#conserve memory by streaming the response to the file system in 1000 byte chunks.
