# need to pip install request module to os

# import modules needed.

import requests
from pprint import pprint  #view returns of pprint
import json   #to handle json responses


print(requests.__version__)
print(requests.__copyright__)

r_get = requests.get('https://www.metaweather.com/api/location/2487956/2020/09/22')
print(r_get.status_code)  #returns the status code "200"

print(type(r_get)) #gives the type of the r_get function

#other functions included:

print(type(r_get.headers))

print(type(r_get.json()))

print(pprint(r_get.headers))  #lets us see what is allowed in the header.


#looking at the body of the response

data = json.loads(r_get.text)  #returns body on GET in json format
print(pprint(data))

print(r_get.is_redirect) # looks to see if there is a redirection of an URL




